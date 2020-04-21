import inspect
from optparse import OptionParser
import re
import json

from strawberry_py.models.http_request import HttpRequest
from strawberry_py.models.http_response import HttpResponse
from strawberry_py.parsers.json_serializer import JsonSerializer

FUNCTION_NAME = 0
FUNCTION_HANDLER = 1

class ControllerHandler:
  __instance = None

  def getinstance():
    if ControllerHandler.__instance == None:
      ControllerHandler.__instance = ControllerHandler()
    return ControllerHandler.__instance

  @property
  def serializers(self):
    return self._serializers

  def __init__(self):
    self.endpoints = []
    self._serializers = {
      'application/json': JsonSerializer
    }
    self.default_content_type = 'application/json'

  def register_controller(self, controller_class, controller_implementation_class):

    endpoints = self.get_controller_endpoints(controller_class, controller_implementation_class)

    for endpoint in endpoints:
      endpoint.controller = controller_implementation_class
      self.endpoints.append(endpoint)

  def get_controller_endpoints(self, controller_class, controller_implementation_class) -> list:
    endpoint_infos = []
    controller_methods = inspect.getmembers(controller_class, inspect.isfunction)
    controller_implementation_methods = inspect.getmembers(controller_implementation_class, inspect.isfunction)

    for method_info in controller_methods:
      if hasattr(method_info[1], 'endpoint_info'):
        endpoint_info = method_info[1].endpoint_info
        endpoint_info.handler = self.get_implementation_method(method_info, controller_implementation_methods)
        if endpoint_info.handler is None:
          print('Error:', 'No implementation method found for route', endpoint_info.http_method, endpoint_info.route)
          continue

        endpoint_info.controller = controller_implementation_class
        endpoint_infos.append(endpoint_info)

    return endpoint_infos

  def get_implementation_method(self, endpoint_method, controller_implementation_methods):
    name_to_find = endpoint_method[0]
    for method_info in controller_implementation_methods:
      controller_implementation_method_name = method_info[0]
      if controller_implementation_method_name == name_to_find:
        return method_info[1]

    return None

  def handleRequest(self, http_request):
    content_type = http_request.headers.get('Content-Type', self.default_content_type)

    if not http_request.body is None:
      http_request.body = self.deserialize_body(http_request, content_type)

    print('Searching for suitable controller...')
    endpoint_call = self.get_controller_endpoint_for_path(http_request)

    http_response = HttpResponse()
    http_response.statusCode = 404
    http_response.body = {
      'message': 'Endpoint not found.'
    }

    if not endpoint_call is None:
      http_response.statusCode = 200 # default, may be changed by endpoint_call
      content_type = http_response.headers.get('Content-Type', self.default_content_type)
      http_response.body = self.serialize_body(endpoint_call.invoke(http_request, http_response), content_type)

    return http_response

  def get_controller_endpoint_for_path(self, http_request):
    for endpoint in self.endpoints:
      endpoint_call = endpoint.try_build_call(http_request)

      if endpoint_call is not None:
        return endpoint_call

    return None

  def get_serializer(self, content_type):
    serializer = None
    if content_type in self.serializers:
      serializer = self.serializers[content_type]()

    if serializer is None:
      print('Error: No serializer found for ', content_type)

    return serializer

  def deserialize_body(self, payload: str, content_type: str) -> object:
    serializer = self.get_serializer(content_type)
    return serializer.deserialize(payload)

  def serialize_body(self, payload: object, content_type: str) -> str:
    serializer = self.get_serializer(content_type)
    return serializer.serialize(payload)

import inspect
import re
from optparse import OptionParser
import json

from strawberry_py.models.http_request import HttpRequest
from strawberry_py.models.http_response import HttpResponse
from strawberry_py.parsers.json_serializer import JsonSerializer
from strawberry_py.parsers.raw_serializer import RawSerializer
from strawberry_py.services.content_serializer import ContentSerializerRegistry
from strawberry_py.models.endpoint_info import EndpointInfo
from strawberry_py.models.endpoint_call import EndpointCall
from strawberry_py.models.api_request import ApiRequest

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
    self.endpoints: List[EndpointInfo] = []
    self._serializers = {
      'application/json': JsonSerializer,
      'text/plain': RawSerializer
    }

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
    print('Searching for suitable controller...')
    endpoint_call = self.get_endpoint_info(http_request)

    http_response = HttpResponse()
    http_response.status_code = 404
    http_response.body = {
      'message': 'Endpoint not found.'
    }

    if endpoint_call is None:
      return http_response

    http_response.status_code = 200 # default, may be changed by endpoint_call

    api_request = ApiRequest.from_http_request(http_request, endpoint_call.endpoint)
    return_value = endpoint_call.invoke(http_request, http_response, api_request)

    accept_header = http_request.headers.get('Accept', None)
    content_type_request_header = http_request.headers.get('Content-Type', None)
    if accept_header is None or accept_header == '*/*':
      accept_header = content_type_request_header

    content_type = http_response.headers.get('Content-Type', accept_header)
    http_response.body = ContentSerializerRegistry.get_instance().serialize(return_value, content_type)

    return http_response

  def get_endpoint_info(self, http_request) -> EndpointCall:
    for endpoint in self.endpoints:
      endpoint_call = endpoint.try_build_call(http_request)

      if endpoint_call is not None:
        return endpoint_call

    return None
import inspect
from optparse import OptionParser
import re
import json

from models.request import Request
from models.response import Response
from models.url_matcher import UrlMatcher

FUNCTION_NAME = 0
FUNCTION_HANDLER = 1

class ControllerHandler:
  __instance = None

  def get_instance():
    if ControllerHandler.__instance == None:
      ControllerHandler.__instance = ControllerHandler()
    return ControllerHandler.__instance

  def __init__(self):
    self.endpoints = []

  def register_controller(self, controller_class):
    endpoints = self.get_controller_endpoints(controller_class)
    print(endpoints)

    for endpoint in endpoints:
      endpoint.controller = controller_class
      self.endpoints.append(endpoint)

  def get_controller_endpoints(self, controller_class) -> list:
    endpoint_infos = []
    controller_methods = inspect.getmembers(controller_class, inspect.isfunction)

    for method_info in controller_methods:
      if hasattr(method_info[1], 'endpoint_info'):
        endpoint_infos.append(method_info[1].endpoint_info)

    return endpoint_infos

  def handleRequest(self, request):
    self.parse_body(request)

    endpoint_call = self.get_controller_endpoint_for_path(request)

    response = Response()
    if endpoint_call == None:
      response.statusCode = 404
      response.body = {
        'message': 'Endpoint not found.'
      }
    else:
      response.body = endpoint_call.invoke(request, response)

    return response

  def get_controller_endpoint_for_path(self, request):
    for endpoint in self.endpoints:
      endpoint_call = endpoint.try_build_call(request)

      if endpoint_call is not None:
        return endpoint_call

    return None

  def parse_body(self, request):
    if 'Content-Type' in request.headers:
      if request.headers['Content-Type'] == 'application/json':
        return json.loads(request.body)
    return request.body

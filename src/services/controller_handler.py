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

 # def check_endpoint_queue(self):
 #   for endpoint_definition in self.queued_endpoints:
 #     controller = self.get_controller(endpoint_definition['func'])
 #     if controller == None:
 #       continue
#
 #     controller['endpoints'].append(endpoint_definition)
 #     self.create_matching_routines(endpoint_definition)
 #     #self.queued_endpoints.remove(endpoint_definition)
#
 # def create_matching_routines(self, endpoint_definition):
 #   route = endpoint_definition['route_data']['path']
 #   endpoint_definition.url_matcher = UrlMatcher(route)

  #def get_controller(self, endpoint_func):
  #  for alias, controller_definition in self.controllers.items():
  #    controller_methods = inspect.getmembers(controller_definition['klass'], inspect.isfunction)
  #    for controller_func_tuple in controller_methods:
  #      if controller_func_tuple[FUNCTION_HANDLER] == endpoint_func:
  #        return controller_definition
  #  return None

    #  print(endpoint_definition['module'], '#### VS #####', ControllerHandler.controllers[name]['module'])
    #  if endpoint_definition['class_name'] == klass.__name__ and endpoint_definition['module'] == ControllerHandler.controllers[name]['module']:
    #    print('registering controller with endpoint')
    #    ControllerHandler.registerEndpoint(endpoint_definition['func'], endpoint_definition['qualified_name'], endpoint_definition['module'], klass)


  #def registerEndpoint(self, func, route_data):
  #  self.queued_endpoints.append({
  #    'func': func,
  #    'route_data': route_data
  #  })
#
  #  self.check_endpoint_queue()

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
    #for alias, controller in self.controllers.items():
    #  for endpoint in controller['endpoints']:
    #    if endpoint['route_data']['method'] != request.method:
    #      continue
#
    #    route_regex = endpoint['route_matcher_pattern']
    #    if not route_regex.match(request.path):
    #      continue
    #    else:
    #      return {
    #        'endpoint': endpoint,
    #        'controller': controller
    #      }
    #return None

  def parse_body(self, request):
    if 'Content-Type' in request.headers:
      if request.headers['Content-Type'] == 'application/json':
        return json.loads(request.body)
    return request.body

import inspect
from models.request import Request
from models.response import Response
from optparse import OptionParser
import re
import json
FUNCTION_HANDLER = 1

class ControllerHandler:
  __instance = None

  def get_instance():
    if ControllerHandler.__instance == None:
      ControllerHandler.__instance = ControllerHandler()
    return ControllerHandler.__instance

  def __init__(self):
    self.controllers = {}
    self.queued_endpoints = []

    return

  def add_controller(self, name, klass):
    self.controllers[name] = {
      'klass': klass,
      'endpoints': []
    }

    self.check_endpoint_queue()

  def check_endpoint_queue(self):
    for endpoint_definition in self.queued_endpoints:
      controller = self.get_controller(endpoint_definition['func'])
      if controller == None:
        continue

      controller['endpoints'].append(endpoint_definition)
      self.create_matching_routines(endpoint_definition)
      #self.queued_endpoints.remove(endpoint_definition)

  def create_matching_routines(self, endpoint_definition):
    path = endpoint_definition['route_data']['path']
    matcher_creator_regex = r"\{[^\}]+\}"
    regex = re.compile(re.sub(matcher_creator_regex, '([^\/]+)', path, 0))
    endpoint_definition['route_matcher_pattern'] = regex

    endpoint_definition['route_matcher_pattern_names'] = []
    matches = re.finditer(matcher_creator_regex, path)
    for matchNum, match in enumerate(matches, start=1):
      endpoint_definition['route_matcher_pattern_names'].append(match.group(0)[1:-1])

  def get_controller(self, endpoint_func):
    for alias, controller_definition in self.controllers.items():
      controller_methods = inspect.getmembers(controller_definition['klass'], inspect.isfunction)
      for controller_func_tuple in controller_methods:
        if controller_func_tuple[FUNCTION_HANDLER] == endpoint_func:
          return controller_definition
    return None

    #  print(endpoint_definition['module'], '#### VS #####', ControllerHandler.controllers[name]['module'])
    #  if endpoint_definition['class_name'] == klass.__name__ and endpoint_definition['module'] == ControllerHandler.controllers[name]['module']:
    #    print('registering controller with endpoint')
    #    ControllerHandler.registerEndpoint(endpoint_definition['func'], endpoint_definition['qualified_name'], endpoint_definition['module'], klass)


  def registerEndpoint(self, func, route_data):
    self.queued_endpoints.append({
      'func': func,
      'route_data': route_data
    })

    self.check_endpoint_queue()

  def handleRequest(self, request):
    controller_endpoint = self.get_controller_endpoint_for_path(request)

    response = Response()
    if controller_endpoint == None:
      response.statusCode = 404
      response.body = {
        'message': "Endpoint not found."
      }
    else:
      controller_klass = controller_endpoint['controller']['klass']
      controller_function = controller_endpoint['endpoint']['func']

      endpoint_args = self.get_path_arguments(controller_endpoint, controller_klass(request, response), request)
      response.body = controller_function(**endpoint_args)

    return response

  def get_controller_endpoint_for_path(self, request):
    for alias, controller in self.controllers.items():
      for endpoint in controller['endpoints']:
        if endpoint['route_data']['method'] != request.ethod:
          continue

        route_regex = endpoint['route_matcher_pattern']
        if not route_regex.match(request.path):
          continue
        else:
          return {
            'endpoint': endpoint,
            'controller': controller
          }
    return None

  def get_path_arguments(self, controller_endpoint, controller_instance, request):
    endpoint_args = {
      'self': controller_instance
    }

    matches = re.finditer(controller_endpoint['endpoint']['route_matcher_pattern'], request.path)
    for matchNum, match in enumerate(matches, start=1):
      for groupNum in range(0, len(match.groups())):
        param_name = controller_endpoint['endpoint']['route_matcher_pattern_names'][groupNum - 1]
        param_value = match.group(groupNum + 1)
        endpoint_args[param_name] = param_value

    if 'body_arg' in controller_endpoint['endpoint']['route_data']:
      endpoint_args[controller_endpoint['endpoint']['route_data']['body_arg']] = self.parse_body(request)

    return endpoint_args

  def parse_body(self, request):
    if 'Content-Type' in request.headers:
      if request.headers['Content-Type'] == 'application/json':
        return json.loads(request.body)
    return request.body

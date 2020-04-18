from models.endpoint_info import EndpointInfo

def http_put(route, body_argument):
  def decorator(controller_method):
    controller_method.endpoint_info = EndpointInfo('PUT', route, controller_method)
    controller_method.endpoint_info.body_argument = body_argument
    return controller_method
  return decorator
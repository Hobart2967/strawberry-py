from models.endpoint_info import EndpointInfo

def http_get(route):
  def decorator(controller_method):
    controller_method.endpoint_info = EndpointInfo('GET', route, controller_method)
    return controller_method
  return decorator
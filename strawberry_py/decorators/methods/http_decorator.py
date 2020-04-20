from models.endpoint_info import EndpointInfo

def http(route, http_method):
  def decorator(controller_method):
    controller_method.endpoint_info = EndpointInfo(http_method, route)
    return controller_method
  return decorator
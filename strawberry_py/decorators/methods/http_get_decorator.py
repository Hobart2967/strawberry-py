from strawberry_py.models.endpoint_info import EndpointInfo

def http_get(route):
  def decorator(controller_method):
    controller_method.endpoint_info = EndpointInfo('GET', route)
    return controller_method
  return decorator
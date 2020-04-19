from models.endpoint_info import EndpointInfo

def http_delete(route):
  def decorator(controller_method):
    controller_method.endpoint_info = EndpointInfo('DELETE', route)
    return controller_method
  return decorator
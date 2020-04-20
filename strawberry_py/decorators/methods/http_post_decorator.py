from models.endpoint_info import EndpointInfo

def http_post(route):
  def decorator(controller_method):
    controller_method.endpoint_info = EndpointInfo('POST', route)
    return controller_method
  return decorator
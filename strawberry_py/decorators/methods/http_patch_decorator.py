from strawberry_py.models.endpoint_info import EndpointInfo

def http_patch(route):
  def decorator(controller_method):
    controller_method.endpoint_info = EndpointInfo('PATCH', route)
    return controller_method
  return decorator
from strawberry_py.services.controller_handler import ControllerHandler

def controller(controller_class):
  def decorator(controller_impl_class):
    ControllerHandler \
      .get_instance() \
      .register_controller(controller_class, controller_impl_class)
    return controller_impl_class
  return decorator
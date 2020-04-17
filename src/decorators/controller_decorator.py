from services.controller_handler import ControllerHandler

def controller():
  def decorator(controller_class):
    ControllerHandler \
      .get_instance() \
      .register_controller(controller_class)
    return controller_class
  return decorator
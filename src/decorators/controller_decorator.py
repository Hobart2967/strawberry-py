from services.controller_handler import ControllerHandler

def controller(name):
  def decorator(klass):
    ControllerHandler.get_instance().add_controller(name, klass)
    return klass
  return decorator
from .util import append_argument_to_method
from models.parameter_source import ParameterSource

def body_parameter(name, required=False, maximum_length=None, minimum_length=None, pattern=None):
  source = ParameterSource.BODY
  def decorator(controller_method):
    append_argument_to_method(controller_method, source, name, required, maximum_length, minimum_length, pattern)
    return controller_method
  return decorator
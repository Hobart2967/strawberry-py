from .util import append_argument_to_method
from strawberry_py.models.parameter_source import ParameterSource

def form_parameter(name, type, required=False, maximum_length=None, minimum_length=None, pattern=None):
  source = ParameterSource.FORM
  def decorator(controller_method):
    append_argument_to_method(controller_method, source, name, type, required, maximum_length, minimum_length, pattern)
    return controller_method
  return decorator
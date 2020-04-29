from .util import append_argument_to_method
from strawberry_py.parameters.parameter_source import ParameterSource

def header_parameter(name, data_type, required=False, maximum_length=None, minimum_length=None, pattern=None):
  source = ParameterSource.HEADER
  def decorator(controller_method):
    append_argument_to_method(controller_method, source, name, data_type, required, maximum_length, minimum_length, pattern)
    return controller_method
  return decorator
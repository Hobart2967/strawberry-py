from strawberry_py.parameters.parameter_info import ParameterInfo

def append_argument_to_method(method, source, name, data_type, required, maximum_length, minimum_length, pattern):
  if not hasattr(method, 'parameter_infos'):
    method.parameter_infos = []
  method.parameter_infos.append(ParameterInfo(source, name, data_type, required, maximum_length, minimum_length, pattern))
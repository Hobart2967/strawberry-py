from models.argument_info import ArgumentInfo

def append_argument_to_method(method, source, name, required, maximum_length, minimum_length, pattern):
  if not hasattr(method, 'argument_infos'):
    method.argument_infos = []
  method.argument_infos.append(ArgumentInfo(source, name, required, maximum_length, minimum_length, pattern))
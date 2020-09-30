from strawberry_py.parameters.parameter_info import ParameterInfo
from typing import Type, List

class ParameterValue:
  def __init__(self, info, parameter_value, is_parsed=False):
    super().__init__()
    self._info = info
    if not is_parsed:
      parameter_value = self.parse_value(parameter_value, self.info.data_type)

    self._parameter_value = parameter_value

  @property
  def info(self) -> ParameterInfo:
    return self._info

  @info.setter
  def info(self, value: ParameterInfo) -> None:
    self._info = value

  @property
  def parameter_value(self) -> object:
    return self._parameter_value

  @parameter_value.setter
  def parameter_value(self, value: object) -> None:
    self._parameter_value = value

  def parse_value(self, value, data_type):
    if value is None:
      return value

    target_type = data_type

    if hasattr(data_type, '__origin__'):
      target_type = data_type.__origin__

    value = target_type(value)

    if hasattr(data_type, '__args__'):
      value = self.parse_nested_values(value, data_type)

    return value

  def parse_nested_values(self, value, data_type):
    if hasattr(data_type, '__origin__'):
      target_type = data_type.__origin__

    generic_arguments = []
    if hasattr(data_type, '__args__'):
      generic_arguments = getattr(data_type, '__args__')

    target_value = value

    if target_type is tuple:
      return self.parse_nested_values_of_tuple(target_value, generic_arguments)

    if target_type is dict:
      return self.parse_nested_values_of_dict(target_value, generic_arguments)

    if target_type is list:
      return self.parse_nested_values_of_list(target_value, generic_arguments)

    return target_value

  def parse_nested_values_of_tuple(self, item: tuple, generic_arguments: List[Type]):
    source_value = list(item)
    target_value = []

    for i in range(len(source_value)):
      tuple_item = source_value[i]
      target_value.append(self.parse_value(tuple_item, generic_arguments[i]))

    return tuple(target_value)

  def parse_nested_values_of_dict(self, item: dict, generic_arguments: List[Type]):
    dict_keys = self.parse_nested_values_of_list(item.keys(), [generic_arguments[0]])
    dict_values = self.parse_nested_values_of_list(item.values(), [generic_arguments[1]])

    target_value = { k:v for k,v in zip(dict_keys, dict_values) }

    return target_value

  def parse_nested_values_of_list(self, lst: list, generic_arguments: List[Type]):
    target_value = []
    for item in lst:
      target_value.append(self.parse_value(item, generic_arguments[0]))

    return target_value
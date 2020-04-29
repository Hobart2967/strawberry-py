from strawberry_py.parameters.parameter_info import ParameterInfo

class ParameterValue:
  def __init__(self, info, parameter_value):
    super().__init__()
    self._info = info
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


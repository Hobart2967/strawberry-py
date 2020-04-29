class ParameterInfo:
  def __init__(self, source: str, name: str, data_type: type, required: bool, maximum_length: int, minimum_length: int, pattern: str):
    super().__init__()

    self._source = source
    self._name = name
    self._data_type = data_type
    self._required = required
    self._maximum_length = maximum_length
    self._minimum_length = minimum_length
    self._pattern = pattern

  @property
  def source(self) -> str:
    return self._source

  @source.setter
  def source(self, value: str) -> None:
    self._source = value

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, value: str) -> None:
    self._name = value

  @property
  def data_type(self) -> type:
    return self._data_type

  @data_type.setter
  def data_type(self, value: type) -> None:
    self._data_type = value

  @property
  def required(self) -> bool:
    return self._required

  @required.setter
  def required(self, value: bool) -> None:
    self._required = value

  @property
  def maximum_length(self) -> int:
    return self._maximum_length

  @maximum_length.setter
  def maximum_length(self, value: int) -> None:
    self._maximum_length = value

  @property
  def minimum_length(self) -> int:
    return self._minimum_length

  @minimum_length.setter
  def minimum_length(self, value: int) -> None:
    self._minimum_length = value

  @property
  def pattern(self) -> str:
    return self._pattern

  @pattern.setter
  def pattern(self, value: str) -> None:
    self._pattern = value
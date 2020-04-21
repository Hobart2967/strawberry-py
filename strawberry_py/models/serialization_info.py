class SerializationInfo:
  @property
  def serialized_name(self):
    return self._serialized_name

  @property
  def serialized_type(self):
    return self._serialized_type

  @property
  def property_name(self):
    return self._property_name

  def __init__(self, serialized_name=None, serialized_type=None, property_name=None):
    super().__init__()

    self._serialized_name = serialized_name
    self._serialized_type = serialized_type
    self._property_name = property_name

  def __str__(self):
    return self.serialized_name + ' <=> ' + self.property_name
class ArgumentInfo():
  def __init__(self, source, name, type, required, maximum_length, minimum_length, pattern):
    super().__init__()

    self.source = source
    self.name = name
    self.type = type
    self.required = required
    self.maximum_length = maximum_length
    self.minimum_length = minimum_length
    self.pattern = pattern
from strawberry_py.decorators.parsing.serialize import serialize

class ServerError:
  @serialize('error', str)
  @property
  def error(self) -> str:
    return self._error

  @error.setter
  def error(self, value) -> None:
    self._error = value

  def __init__(self, error_message: str):
    super().__init__()
    self._error = error_message
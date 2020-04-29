from typing import List
from strawberry_py.decorators.parsing.serialize import serialize

class ValidationErrorResponse:
  def __init__(self, messages: List[str]):
    super().__init__()
    self._messages = messages

  @property
  @serialize('messages', List[str])
  def messages(self) -> List[str]:
    return self._messages

  @messages.setter
  def messages(self, value: List[str]) -> None:
    self._messages = value
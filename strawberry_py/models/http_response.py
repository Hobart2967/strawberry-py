class HttpResponse:
  def __init__(self):
    super().__init__()
    self._status_code = 200
    self._status_message = 'OK'
    self._body = None
    self._headers = {}

  @property
  def status_code(self) -> int:
    return self._status_code

  @status_code.setter
  def status_code(self, value: int) -> None:
    self._status_code = value

  @property
  def status_message(self) -> str:
    return self._status_message

  @status_message.setter
  def status_message(self, value: str) -> None:
    self._status_message = value

  @property
  def body(self) -> object:
    return self._body

  @body.setter
  def body(self, value: object) -> None:
    self._body = value

  @property
  def headers(self) -> dict:
    return self._headers

  @headers.setter
  def headers(self, value: dict) -> None:
    self._headers = value
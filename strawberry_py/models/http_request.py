class HttpRequest:
  def __init__(self):
    self._headers = None
    self._path = None
    self._user_agent = None
    self._http_method = None
    self._query_string = None
    self._body = None

  @property
  def headers(self) -> dict:
    return self._headers

  @headers.setter
  def headers(self, value: dict) -> None:
    self._headers = value

  @property
  def path(self) -> str:
    return self._path

  @path.setter
  def path(self, value: str) -> None:
    self._path = value

  @property
  def user_agent(self) -> str:
    return self._user_agent

  @user_agent.setter
  def user_agent(self, value: str) -> None:
    self._user_agent = value

  @property
  def http_method(self) -> str:
    return self._http_method

  @http_method.setter
  def http_method(self, value: str) -> None:
    self._http_method = value

  @property
  def query_string(self) -> dict:
    return self._query_string

  @query_string.setter
  def query_string(self, value: dict) -> None:
    self._query_string = value

  @property
  def body(self) -> object:
    return self._body

  @body.setter
  def body(self, value: object) -> None:
    self._body = value
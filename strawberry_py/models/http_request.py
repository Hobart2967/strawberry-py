class HttpRequest:
  def __init__(self):
    self.headers = None
    self.path = None
    self.user_agent = None
    self.http_method = None
    self.query_string = None
    self.body = None
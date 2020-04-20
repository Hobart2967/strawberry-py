class HttpResponse:
  def __init__(self):
    super().__init__()
    self.statusCode = 200
    self.statusMessage = 'OK'
    self.body = None
    self.headers = {}
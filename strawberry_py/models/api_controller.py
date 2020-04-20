class ApiController:
  def __init__(self, request, response):
    super().__init__()
    self.request = request
    self.response = response
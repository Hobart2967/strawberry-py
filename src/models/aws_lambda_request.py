from .http_request import HttpRequest

class AwsLambdaRequest(HttpRequest):
  def __init__(self, event, context):
    super().__init__()
    self.event = event
    self.context = context
    self.parse()

  def parse(self):
    self.headers = self.event['headers']
    self.path = self.event['path']
    self.user_agent = self.event['requestContext']['identity']['userAgent']
    self.method = self.event['httpMethod']
    self.query_string = self.event['queryStringParameters']
    self.body = self.event['body']

  def __str__(self):
    return str({
      'headers': self.headers,
      'path': self.path,
      'user_agent': self.user_agent,
      'method': self.method,
      'query_string': self.query_string,
      'body': self.body
    })

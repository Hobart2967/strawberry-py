from strawberry_py.models.http_response import HttpResponse
import json

class AwsLambdaResponse(HttpResponse):

  @staticmethod
  def from_response(response):
    aws_response = AwsLambdaResponse()
    aws_response.status_code = response.status_code
    aws_response.headers = response.headers
    aws_response.body = response.body
    return aws_response

  def get_lambda_result(self):
    return {
      'statusCode': self.status_code,
      'headers': self.headers,
      'body': self.body
    }
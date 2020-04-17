from .response import Response
import json

class AwsLambdaResponse(Response):
  def from_response(response):
    aws_response = AwsLambdaResponse()
    aws_response.statusCode = response.statusCode
    aws_response.headers = response.headers
    aws_response.body = response.body
    return aws_response

  def get_lambda_result(self):
    return {
      'statusCode': self.statusCode,
      'headers': self.headers,
      'body': json.dumps(self.body)
    }
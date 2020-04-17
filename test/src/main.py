import os
import sys
sys.path.insert(0, os.path.join(os.getcwd(), os.path.dirname(__file__), '..', '..', 'src'))
from strawberry_py import ControllerHandler, AwsLambdaRequest, AwsLambdaResponse

#region Controllers
from .controllers.hello_world_controller import HelloWorldController
#endregion

def handler(event, context):
  request = AwsLambdaRequest(event, context)
  controller_handler = ControllerHandler.get_instance()
  response = controller_handler.handleRequest(request)

  return AwsLambdaResponse.from_response(response).get_lambda_result()
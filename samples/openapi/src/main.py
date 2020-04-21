import os
import sys
sys.path.insert(0, os.path.join(os.getcwd(), os.path.dirname(__file__), '..', '..', '..'))
from strawberry_py import ControllerHandler, AwsLambdaRequest, AwsLambdaResponse

#region Controllers
from src.controllers.pet_api_controller_impl import PetApiControllerImpl
from src.controllers.store_api_controller_impl import StoreApiControllerImpl
from src.controllers.user_api_controller_impl import UserApiControllerImpl
#endregion

def handler(event, context):
  http_request = AwsLambdaRequest(event, context)
  http_response = handle_http_request(http_request)

  aws_lambda_response = AwsLambdaResponse.from_response(http_response)
  return aws_lambda_response.get_lambda_result()

def handle_http_request(http_request):
  controller_handler = ControllerHandler.getinstance()
  http_response = controller_handler.handleRequest(http_request)
  return http_response

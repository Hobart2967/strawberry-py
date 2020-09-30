import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), os.path.dirname(__file__), '..', '..', '..'))
from strawberry_py import ControllerHandler, AwsLambdaRequest, AwsLambdaResponse
# from strawberry_py import ControllerHandler, AwsLambdaRequest, AwsLambdaResponse

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

"""
multipart payload
{
	'headers': {
		'Content-Type': 'multipart/form-data; boundary=--------------------------978974156610236089704874',
		'apiKey': '20',
		'User-Agent': 'PostmanRuntime/7.24.1',
		'Accept': '*/*',
		'Cache-Control': 'no-cache',
		'Postman-Token': '8c42147d-9119-4a60-8f14-840dec078212',
		'Host': 'localhost:3000',
		'Accept-Encoding': 'gzip, deflate, br',
		'Connection': 'keep-alive',
		'Content-Length': 382
	},
	'path': '/v2/pet/123',
	'pathParameters': {
		'proxy': 'v2%2Fpet%2F123'
	},
	'requestContext': {
		'accountId': 'offlineContext_accountId',
		'resourceId': 'offlineContext_resourceId',
		'apiId': 'offlineContext_apiId',
		'stage': 'dev',
		'requestId': 'offlineContext_requestId_',
		'identity': {
			'cognitoIdentityPoolId': 'offlineContext_cognitoIdentityPoolId',
			'accountId': 'offlineContext_accountId',
			'cognitoIdentityId': 'offlineContext_cognitoIdentityId',
			'caller': 'offlineContext_caller',
			'apiKey': 'offlineContext_apiKey',
			'sourceIp': '127.0.0.1',
			'cognitoAuthenticationType': 'offlineContext_cognitoAuthenticationType',
			'cognitoAuthenticationProvider': 'offlineContext_cognitoAuthenticationProvider',
			'userArn': 'offlineContext_userArn',
			'userAgent': 'PostmanRuntime/7.24.1',
			'user': 'offlineContext_user'
		},
		'authorizer': {
			'principalId': 'offlineContext_authorizer_principalId'
		},
		'resourcePath': '/{proxy*}',
		'httpMethod': 'POST'
	},
	'resource': '/{proxy*}',
	'httpMethod': 'POST',
	'queryStringParameters': {
		'TestKey': ['12', '11']
	},
	'stageVariables': None,
	'body': '----------------------------978974156610236089704874\r\nContent-Disposition: form-data; name="name"\r\n\r\nDampf\r\n----------------------------978974156610236089704874\r\nContent-Disposition: form-data; name="firstName"\r\n\r\nHans\r\n----------------------------978974156610236089704874\r\nContent-Disposition: form-data; name="test"\r\n\r\n123\r\n----------------------------978974156610236089704874--\r\n',
	'isOffline': True
}
"""
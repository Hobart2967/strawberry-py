from strawberry_py.util.to_snake_case import to_snake_case
from strawberry_py.util.log import Log
from strawberry_py.results.validation_error_response import ValidationErrorResponse
from strawberry_py.models.api_request import ApiRequest
from strawberry_py.models.http_request import HttpRequest
from strawberry_py.models.http_response import HttpResponse

class EndpointCall:
  @property
  def endpoint(self) -> 'strawberry_py.models.EndpointInfo':
    return self._endpoint

  @endpoint.setter
  def endpoint(self, value: 'strawberry_py.models.EndpointInfo') -> None:
    self._endpoint = value

  def __init__(self, endpoint, endpoint_arguments):
    self._endpoint = endpoint
    self.endpoint_arguments = endpoint_arguments

  def invoke(self, request: HttpRequest, response: HttpResponse, api_request: ApiRequest):
    controller = self.endpoint.controller(request, response)

    args = {
      'self': controller,
    }

    for parameter in api_request.parameters:
      Log.debug('Extending call args by parameter', parameter.info.name, 'as method argument', to_snake_case(parameter.info.name))
      args[to_snake_case(parameter.info.name)] = parameter.parameter_value

    Log.debug('Validating Request...')
    validation_errors = api_request.validate()
    if len(validation_errors) > 0:
      response.status_code = 400
      Log.info('Request was not validated successfully. Returning validation errors')
      return ValidationErrorResponse(validation_errors)

    Log.debug('Calling', self.endpoint.handler.__name__, 'on', self.endpoint.controller.__name__, 'with arguments', args)

    return self.endpoint.handler(**args)

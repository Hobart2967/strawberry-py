class EndpointCall:
  def __init__(self, endpoint, endpoint_arguments):
    self.endpoint = endpoint
    self.endpoint_arguments = endpoint_arguments

  def invoke(self, request, response):
    controller = self.endpoint.controller(request, response)
    args = {
      **self.endpoint_arguments.route_parameters,
      **{ 'self': controller },
      **self.endpoint_arguments.query_string_parameters,
      **self.endpoint_arguments.form_parameters,
      **self.endpoint_arguments.body_parameters
    }
    print(args)
    return self.endpoint.handler(**args)
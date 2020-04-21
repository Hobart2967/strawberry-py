class RequestMatchResult:
  def __init__(self, matcher, route_parameters, form_parameters, query_string_parameters, body_parameters):
    self.route_parameters = route_parameters
    self.query_string_parameters = query_string_parameters
    self.form_parameters = form_parameters
    self.body_parameters = body_parameters
    self.matcher = matcher
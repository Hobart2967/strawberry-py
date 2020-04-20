class UrlMatchResult:
  def __init__(self, matcher, route_parameters):
    self.route_parameters = route_parameters
    self.matcher = matcher
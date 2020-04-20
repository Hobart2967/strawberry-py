from models.url_matcher import UrlMatcher
from models.endpoint_call import EndpointCall

class EndpointInfo:
  def __init__(self, http_method, route):
    self.http_method = http_method
    self.route = route
    self.matcher = UrlMatcher(route, http_method)
    self.controller = None
    self.handler = None
    self.body_argument = None

  def __str__(self):
    return self.http_method + ' ' + self.route

  def try_build_call(self, request) -> EndpointCall:
    possible_match = self.matcher.try_get_match(request)
    if possible_match is None:
      return None

    if self.body_argument is not None:
      possible_match.route_parameters[self.body_argument] = request.body

    return EndpointCall(self, possible_match)
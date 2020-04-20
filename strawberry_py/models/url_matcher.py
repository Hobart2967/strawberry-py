from models.url_match_result import UrlMatchResult
from util.to_snake_case import to_snake_case

from typing import Pattern
import re

class UrlMatcher:
  def __init__(self, route, http_method):
    self.route = route
    self.http_method = http_method
    self.param_name_regex = r"\{[^\}]+\}"
    self.matcher_regex = self._get_regex()
    self._load_route_params()

  def try_get_match(self, request) -> UrlMatchResult:
    if self.http_method != request.http_method:
      return None

    if not self.matcher_regex.match(request.path):
      return None

    parameter_values = self.get_route_parameter_values(request)
    return UrlMatchResult(self, parameter_values)

  def _get_regex(self) -> Pattern:
    return re.compile('^' + re.sub(self.param_name_regex, '([^/]+)', self.route, 0) + '$')

  def _load_route_params(self) -> None:
    self._route_params = []
    matches = re.finditer(self.param_name_regex, self.route)
    for matchNum, match in enumerate(matches, start=1):
      self._route_params.append(match.group(0)[1:-1])

  def get_route_parameter_values(self, request):
    route_params = {}

    matches = re.finditer(self.matcher_regex, request.path)
    for matchNum, match in enumerate(matches, start=1):
      for groupNum in range(0, len(match.groups())):
        param_name = self._route_params[groupNum - 1]
        param_value = match.group(groupNum + 1)
        route_params[to_snake_case(param_name)] = param_value

    return route_params

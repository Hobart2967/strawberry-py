from strawberry_py.models.request_match_result import RequestMatchResult
from strawberry_py.util.to_snake_case import to_snake_case
from strawberry_py.models.http_request import HttpRequest

from typing import Pattern
import re

class RequestMatcher:
  @property
  def endpoint_info(self) -> 'EndpointInfo':
    return self._endpoint_info

  @property
  def http_method(self) -> str:
    return self._http_method

  @property
  def param_name_regex(self) -> Pattern:
    return self._param_name_regex

  @property
  def matcher_regex(self) -> Pattern:
    return self._matcher_regex


  def __init__(self, endpoint_info: 'EndpointInfo', http_method: str):
    self._endpoint_info = endpoint_info
    self._http_method = http_method
    self._param_name_regex = r"\{[^\}]+\}"
    self._matcher_regex = self._get_regex()
    self._load_route_params()

  def try_get_match(self, request: HttpRequest) -> RequestMatchResult:
    if self.http_method != request.http_method:
      return None

    if not self.matcher_regex.match(request.path):
      return None

    route_parameter_values = self.get_route_parameter_values(request)
    query_string_parameter_values = self.get_query_string_parameter_values(request)
    form_parameter_values = self.get_form_parameter_values(request)
    body_parameter_values = self.get_body_parameter_values(request)

    return RequestMatchResult(self, route_parameter_values, form_parameter_values, query_string_parameter_values, body_parameter_values)

  def get_form_parameter_values(self, request: HttpRequest):
    return {}

  def get_body_parameter_values(self, request: HttpRequest):
    return {}

  def get_query_string_parameter_values(self, request: HttpRequest):
    print(request.query_string)
    return {}

  def _get_regex(self) -> Pattern:
    return re.compile('^' + re.sub(self.param_name_regex, '([^/]+)', self.endpoint_info.route, 0) + '$')

  def _load_route_params(self) -> None:
    self._route_params = []
    matches = re.finditer(self.param_name_regex, self.endpoint_info.route)
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

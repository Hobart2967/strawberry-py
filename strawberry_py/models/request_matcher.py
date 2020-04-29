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
  def matcher_regex(self) -> Pattern:
    return self._matcher_regex

  def __init__(self, endpoint_info: 'EndpointInfo', http_method: str):
    self._endpoint_info = endpoint_info
    self._http_method = http_method
    self._param_name_regex = r"\{[^\}]+\}"
    self._matcher_regex = self._get_regex()

  def try_get_match(self, request: HttpRequest) -> RequestMatchResult:
    if self.http_method != request.http_method:
      return None

    if not self.matcher_regex.match(request.path):
      return None

    return RequestMatchResult(self)

  def _get_regex(self) -> Pattern:
    return re.compile('^' + re.sub(self._param_name_regex, '([^/]+)', self.endpoint_info.route, 0) + '$')

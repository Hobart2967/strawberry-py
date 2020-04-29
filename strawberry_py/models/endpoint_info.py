from typing import Callable, List

from strawberry_py.models.request_matcher import RequestMatcher
from strawberry_py.models.endpoint_call import EndpointCall
from strawberry_py.parameters.parameter_info import ParameterInfo

class EndpointInfo:
  @property
  def http_method(self) -> str:
    return self._http_method

  @property
  def route(self) -> str:
    return self._route

  @property
  def matcher(self) -> RequestMatcher:
    return self._matcher

  @property
  def controller(self) -> type:
    return self._controller

  @controller.setter
  def controller(self, value: type) -> None:
    self._controller = value

  @property
  def handler(self) -> Callable:
    return self._handler

  @property
  def parameter_infos(self) -> List[ParameterInfo]:
    handler_name = self._handler.__name__
    definition_handler = getattr(self._controller.controller_definition, handler_name)
    parameter_infos_collection = []

    if hasattr(definition_handler, 'parameter_infos'):
        parameter_infos_collection = parameter_infos_collection + getattr(definition_handler, 'parameter_infos')

    if hasattr(self._handler, 'parameter_infos'):
        parameter_infos_collection = parameter_infos_collection + getattr(self._handler, 'parameter_infos')

    return parameter_infos_collection

  @handler.setter
  def handler(self, value: Callable) -> None:
    self._handler = value

  def __init__(self, http_method, route):
    self._http_method = http_method
    self._route = route
    self._matcher = RequestMatcher(self, http_method)
    self._controller = None
    self._handler = None

  def __str__(self):
    return self.http_method + ' ' + self.route

  def try_build_call(self, request) -> EndpointCall:
    possible_match = self.matcher.try_get_match(request)
    if possible_match is None:
      return None

    return EndpointCall(self, possible_match)
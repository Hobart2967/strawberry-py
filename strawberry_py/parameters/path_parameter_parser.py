from abc import abstractmethod, ABCMeta
from typing import List
import re

from strawberry_py.models.http_request import HttpRequest
from strawberry_py.parameters.parameter_value import ParameterValue
from strawberry_py.parameters.parameter_info import ParameterInfo
from strawberry_py.parameters.parameter_parser import ParameterParser
from strawberry_py.services.content_serializer import ContentSerializerRegistry
from strawberry_py.parameters.parameter_source import ParameterSource
from strawberry_py.util.to_snake_case import to_snake_case
from strawberry_py.util.log import Log

class PathParameterParser(ParameterParser):
  def __init__(self, route_definition):
    super().__init__()

    self._route_definition = route_definition
    self.content_serializer = ContentSerializerRegistry.get_instance()
    self._param_name_regex = r"\{[^\}]+\}"

  def get_parameters(self, http_request: HttpRequest, parameter_infos: List[ParameterInfo]) -> List[ParameterValue]:
    path_parameter_values = self.get_path_parameter_values(http_request)

    path_parameter_infos = list(filter(lambda item: item.source == ParameterSource.PATH, parameter_infos))
    return list(map(lambda item: self.get_value_from(http_request, item), path_parameter_infos))

  def get_value_from(self, http_request, parameter_info):
    python_property_name = to_snake_case(parameter_info.name)
    Log.debug('Finding parameter value for', parameter_info.name, 'aka', python_property_name)

    values = self.get_path_parameter_values(http_request)
    raw_parameter_value = values[python_property_name]
    return ParameterValue(parameter_info, raw_parameter_value)

  def load_path_parameter_names(self) -> List[object]:
    path_parameter_names = []
    matches = re.finditer(self._param_name_regex, self._route_definition)
    for matchNum, match in enumerate(matches, start=1):
      path_parameter_names.append(match.group(0)[1:-1])

    Log.debug('Recognized path parameter names', path_parameter_names, 'in route', self._route_definition)

    return path_parameter_names

  def get_path_parameter_values(self, request: HttpRequest):
    route_parameter_values = self.load_path_parameter_names()
    route_params = {}

    matcher_regex = re.compile('^' + re.sub(self._param_name_regex, '([^/]+)', self._route_definition, 0) + '$')

    matches = re.finditer(matcher_regex, request.path)
    for matchNum, match in enumerate(matches, start=1):
      for groupNum in range(0, len(match.groups())):
        param_name = route_parameter_values[groupNum - 1]
        param_value = match.group(groupNum + 1)
        route_params[to_snake_case(param_name)] = param_value

    Log.debug('Recognized path parameter values', route_params, 'for request path', request.path, 'matching the route', self._route_definition)
    return route_params
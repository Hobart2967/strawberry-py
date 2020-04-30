from abc import abstractmethod, ABCMeta
from typing import List
import re
from urllib.parse import parse_qs

from strawberry_py.models.http_request import HttpRequest
from strawberry_py.parameters.parameter_value import ParameterValue
from strawberry_py.parameters.parameter_info import ParameterInfo
from strawberry_py.parameters.parameter_parser import ParameterParser
from strawberry_py.services.content_serializer import ContentSerializerRegistry
from strawberry_py.parameters.parameter_source import ParameterSource
from strawberry_py.util.to_snake_case import to_snake_case
from strawberry_py.util.log import Log

class QueryStringParameterParser(ParameterParser):
  def __init__(self):
    super().__init__()

    self.content_serializer = ContentSerializerRegistry.get_instance()

  def get_parameters(self, http_request: HttpRequest, parameter_infos: List[ParameterInfo]) -> List[ParameterValue]:
    query_string_parameter_infos = list(filter(lambda item: item.source == ParameterSource.QUERY_STRING, parameter_infos))
    return list(map(lambda item: self.get_value_from(http_request, item, http_request.query_string), query_string_parameter_infos))

  def get_value_from(self, http_request, parameter_info: ParameterInfo, query_string: dict):
    if (query_string is None) or (not parameter_info.name in query_string):
      return ParameterValue(parameter_info, None)

    raw_parameter_value = query_string.get(parameter_info.name, None)

    return ParameterValue(parameter_info, raw_parameter_value)
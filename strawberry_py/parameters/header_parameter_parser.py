from abc import abstractmethod, ABCMeta
from strawberry_py.models.http_request import HttpRequest
from typing import List
from strawberry_py.parameters.parameter_value import ParameterValue
from strawberry_py.parameters.parameter_info import ParameterInfo
from strawberry_py.parameters.parameter_parser import ParameterParser
from strawberry_py.parameters.parameter_source import ParameterSource
from strawberry_py.services.content_serializer import ContentSerializerRegistry
import re

class HeaderParameterParser(ParameterParser):
  def __init__(self):
    super().__init__()

    self.content_serializer = ContentSerializerRegistry.get_instance()
    self._param_name_regex = r"\{[^\}]+\}"

  def get_parameters(self, http_request: HttpRequest, parameter_infos: List[ParameterInfo]) -> List[ParameterValue]:
    header_parameter_infos = list(filter(lambda item: item.source == ParameterSource.HEADER, parameter_infos))

    return list(map(lambda item: self.get_value_from(http_request, item), header_parameter_infos))

  def get_value_from(self, http_request, parameter_info: ParameterInfo):
    if (http_request.headers is None) or (not parameter_info.name in http_request.headers):
      return ParameterValue(parameter_info, None)

    raw_parameter_value = http_request.headers.get(parameter_info.name, None)
    parsed_parameter_value = parameter_info.data_type(raw_parameter_value)
    return ParameterValue(parameter_info, parsed_parameter_value)
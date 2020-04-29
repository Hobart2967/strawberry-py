from abc import abstractmethod, ABCMeta
from strawberry_py.models.http_request import HttpRequest
from typing import List
from strawberry_py.parameters.parameter_value import ParameterValue
from strawberry_py.parameters.parameter_info import ParameterInfo
from strawberry_py.parameters.parameter_parser import ParameterParser
from strawberry_py.parameters.parameter_source import ParameterSource
from strawberry_py.services.content_serializer import ContentSerializerRegistry
import re

class FormParameterParser(ParameterParser):
  def __init__(self,):
    super().__init__()

    self.content_serializer = ContentSerializerRegistry.get_instance()
    self._param_name_regex = r"\{[^\}]+\}"

  def get_parameters(self, http_request: HttpRequest, parameter_infos: List[ParameterInfo]) -> List[ParameterValue]:
    form_parameter_infos = list(filter(lambda item: item.source == ParameterSource.FORM, parameter_infos))

    return [] # map(lambda item: self.get_value_from(http_request, item), path_parameter_infos)

  def get_value_from(self, http_request, parameter_info):
    value = http_request.headers.get(parameter_info.serialized_name, None)

    return ParameterValue(parameter_info.name, parameter_info.data_type, parameter_info.location, value)
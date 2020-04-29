from abc import abstractmethod, ABCMeta
from typing import List

from strawberry_py.models.http_request import HttpRequest
from strawberry_py.parameters.parameter_value import ParameterValue
from strawberry_py.parameters.parameter_info import ParameterInfo
from strawberry_py.parameters.parameter_parser import ParameterParser
from strawberry_py.services.content_serializer import ContentSerializerRegistry
from strawberry_py.parameters.parameter_source import ParameterSource

class BodyParameterParser(ParameterParser):
  def __init__(self):
    super().__init__()
    self.content_serializer = ContentSerializerRegistry.get_instance()

  def get_parameters(self, http_request: HttpRequest, parameter_infos: List[ParameterInfo]) -> List[ParameterValue]:
    body_parameter_infos = list(filter(lambda item: item.source == ParameterSource.BODY, parameter_infos))

    return list(map(lambda item: self.get_value_from(http_request, item), body_parameter_infos))

  def get_value_from(self, http_request, parameter_info):
    mine_type = http_request.headers.get('Content-Type', None)
    value = self.content_serializer.deserialize(http_request.body, mine_type, parameter_info.data_type)

    return ParameterValue(parameter_info.name, parameter_info.data_type, parameter_info.location, value)
from abc import abstractmethod, ABCMeta
from typing import List

from strawberry_py.models.http_request import HttpRequest
from strawberry_py.parameters.parameter_info import ParameterInfo
from strawberry_py.parameters.parameter_value import ParameterValue

class ParameterParser(metaclass=ABCMeta):
  @abstractmethod
  def get_parameters(self, http_request: HttpRequest, parameter_infos: List[ParameterInfo]) -> ParameterValue:
    pass
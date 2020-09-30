import itertools
import re
from typing import List

from strawberry_py.models.http_request import HttpRequest
from strawberry_py.parameters.path_parameter_parser import PathParameterParser
from strawberry_py.parameters.body_parameter_parser import BodyParameterParser
from strawberry_py.parameters.form_parameter_parser import FormParameterParser
from strawberry_py.parameters.header_parameter_parser import HeaderParameterParser
from strawberry_py.parameters.query_string_parameter_parser import QueryStringParameterParser
from strawberry_py.parameters.parameter_value import ParameterValue
from strawberry_py.util.log import Log

class ApiRequest:
  def __init__(self, parameters: List[ParameterValue]):
    self._parameters = parameters

  @staticmethod
  def from_http_request(http_request: HttpRequest, endpoint_info: 'strawberry_py.models.EndpointInfo') -> 'ApiRequest':
    parameters = []

    all_parameters = [
      PathParameterParser(endpoint_info.route).get_parameters(http_request, endpoint_info.parameter_infos),
      FormParameterParser().get_parameters(http_request, endpoint_info.parameter_infos),
      BodyParameterParser().get_parameters(http_request, endpoint_info.parameter_infos),
      HeaderParameterParser().get_parameters(http_request, endpoint_info.parameter_infos),
      QueryStringParameterParser().get_parameters(http_request, endpoint_info.parameter_infos),
    ]
    all_parameters = list(itertools.chain(*all_parameters))
    return ApiRequest(all_parameters)

  @property
  def parameters(self) -> List[ParameterValue]:
    return self._parameters

  @parameters.setter
  def parameters(self, value: List[ParameterValue]) -> None:
    self._parameters = value

  def validate(self) -> bool:
    validation_messages = []

    missing_required_parameters = list(filter(lambda parameter: parameter.parameter_value is None and parameter.info.required == True, self.parameters))
    if len(missing_required_parameters) > 0:
      missing_required_parameter_names = list(map(lambda parameter: 'Missing required parameter ' + parameter.info.name, missing_required_parameters))
      Log.debug('ValidationError:', missing_required_parameter_names)
      validation_messages = itertools.chain(validation_messages, missing_required_parameter_names)

    too_short_values = list(filter(lambda parameter: type(parameter.parameter_value) is str \
                                                     and parameter.info.minimum_length is not None \
                                                     and (parameter.parameter_value is None
                                                          or len(parameter.parameter_value) < parameter.info.minimum_length), self.parameters))
    if len(too_short_values) > 0:
      too_short_value_names = list(map(
        lambda parameter: 'Parameter ' + parameter.info.name + ' is not exceeding minimum length with value "' + parameter.parameter_value + '"',
        too_short_values))
      Log.debug('ValidationError:', too_short_value_names)
      validation_messages = itertools.chain(validation_messages, too_short_value_names)

    too_long_values = list(filter(lambda parameter: type(parameter.parameter_value) is str \
                                                    and parameter.info.maximum_length is not None \
                                                    and parameter.parameter_value is not None \
                                                    and len(parameter.parameter_value) > parameter.info.maximum_length , self.parameters))
    if len(too_long_values) > 0:
      too_long_values = list(map(
        lambda parameter: 'Parameter ' + parameter.info.name + ' is exceeding maximum length with value "' + parameter.parameter_value + '"',
        too_long_values))
      Log.debug('ValidationError:', too_long_values)
      validation_messages = itertools.chain(validation_messages, too_long_values)


    not_matching_values = list(filter(lambda parameter: self.check_pattern(parameter), self.parameters))
    if len(not_matching_values) > 0:
      not_matching_value_names = list(map(lambda parameter: 'Value \'' + parameter.parameter_value + \
                                                            '\' for parameter ' + parameter.info.name + \
                                                            ' is not matching pattern \'' + \
                                                            parameter.info.pattern + '\'', not_matching_values))
      Log.debug('ValidationError:', not_matching_value_names)
      validation_messages = itertools.chain(validation_messages, not_matching_value_names)

    return list(validation_messages)

  def check_pattern(self, parameter: ParameterValue) -> bool:
    if type(parameter.parameter_value) != str:
      return False

    if parameter.info.pattern is None:
      return False

    regex = re.compile(parameter.info.pattern)
    matches = bool(regex.match(parameter.parameter_value))
    return not matches
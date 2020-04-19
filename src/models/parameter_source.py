from enum import Enum
class ParameterSource(Enum):
    QUERY_STRING = 1
    PATH = 2
    HEADER = 3
    BODY = 4
    FORM = 5
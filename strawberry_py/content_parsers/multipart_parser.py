import re
from strawberry_py.content_parsers.multipart_element import MultipartElement

class MultipartParser:
  def __init__(self, boundary_key, body):
    super().__init__()
    self._boundary_key = boundary_key
    self._elements = None

    self.parse_body(body)

  @property
  def boundary(self) -> str:
    return self._boundary_key

  @boundary.setter
  def boundary(self, value: str) -> None:
    self._boundary_key = value

  def parse_body(self, body) -> None:
    self._elements = []
    self._body = body

    """
    The boundary delimiter line is then defined as a line
    consisting entirely of
     - two hyphen characters ("-", decimal value 45)
     - followed by the boundary parameter value from the Content-Type header field,
     - optional linear whitespace, and a terminating CRLF.
    """

    split_regex = re.compile('--' + self._boundary_key + '[ ]{0,1}[\\r]{0,1}\\n')
    raw_elements = split_regex.split(self._body)
    raw_elements = list(filter(lambda element: self.is_not_empty(element), raw_elements))

    termination_element = raw_elements[len(raw_elements) - 1]
    termination_regex_str = '--' + self._boundary_key + '--[ ]{0,1}[\\r]{0,1}\\n'
    termination_regex = re.compile(termination_regex_str)

    if not termination_regex.search(termination_element):
      raise Exception('Could not find boundary termination in body')

    raw_elements[len(raw_elements) - 1] = termination_regex.split(termination_element)[0]
    print('start', raw_elements)
    raw_elements = list(map(lambda element: self.remove_ending_crlf(element), raw_elements))

    return list(map(lambda element: MultipartElement(element), raw_elements))

  def remove_ending_crlf(self, input_string: str):
    if (input_string[-2:] == '\r\n'):
      return input_string[0: -2]
    return input_string

  def is_not_empty(self, input_string: str):
    return input_string != ''



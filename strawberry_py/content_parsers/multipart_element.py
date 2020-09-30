from typing import Any
from io import BytesIO
import base64
from strawberry_py.content_parsers.content_disposition_header import ContentDispositionHeader

class MultipartElement:
    @property
    def content_disposition(self) -> ContentDispositionHeader:
        return self._content_disposition

    @content_disposition.setter
    def content_disposition(self, value: ContentDispositionHeader) -> None:
        self._content_disposition = value

    @property
    def headers(self) -> dict:
        return self._headers

    @headers.setter
    def headers(self, value: dict) -> None:
        self._headers = value

    @property
    def content(self) -> Any:
          return self._content

    @content.setter
    def content(self, value: Any) -> None:
        self._content = value


    def __init__(self, raw_element):
        super().__init__()
        self._raw_element = None
        self._headers = None
        self._content = None
        self.parse_element(raw_element)


    def parse_element(self, raw_element) -> None:
        self._raw_element = raw_element
        self.parse_headers()
        self.parse_content()

    def parse_content(self) -> None:
        header_seperator_index = self._raw_element.find('\r\n\r\n')
        element_body = self._raw_element[header_seperator_index+4:]

        self.content = BytesIO(bytes(element_body, 'ISO-8859-1', errors='surrogatepass'))
        with open('./test.png', 'wb') as a:
            a.write(self.content.getvalue())

    def parse_headers(self) -> None:
        self.headers = {}
        header_seperator_index = self._raw_element.find('\r\n\r\n')
        raw_element_headers = self._raw_element[0:header_seperator_index]
        element_headers = raw_element_headers.splitlines()
        for header_line in element_headers:
            header_pair = header_line.split(':')
            if header_pair[0] == 'Content-Disposition':
              self._content_disposition = ContentDispositionHeader(header_pair[1])
            self.headers[header_pair[0]] = header_pair[1].strip(' ')





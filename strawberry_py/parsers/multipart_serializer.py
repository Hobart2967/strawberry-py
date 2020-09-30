import json
from strawberry_py.content_parsers.multipart_parser import MultipartParser
from strawberry_py.parsers.dict_serializer import DictSerializer
from strawberry_py.parsers.serializer import Serializer

class MultipartSerializer(Serializer):
    def serialize(self, value: object) -> str:
        dict_serializer = DictSerializer()
        serialized_json_dict = dict_serializer.serialize(value)
        return json.dumps(serialized_json_dict)

    def deserialize(self, value: str, target_class: type, mime_type: str) -> object:
      content_type_header = mime_type.split(';')
      boundary = None
      for header_part in content_type_header:
        split_header_part = header_part.split('=')
        if split_header_part[0].strip(' ') != 'boundary':
          continue

        boundary = split_header_part[1]

      if boundary is None:
        raise Exception('No boundary found in Content-Type header')
      print('HEADER', mime_type)
      print('BODYBODYBODYBODYBODYBODY\n', value, '\nBODYBODYBODYBODYBODYBODYBODYBODYBODY')
      parser = MultipartParser(boundary, value)

      return None
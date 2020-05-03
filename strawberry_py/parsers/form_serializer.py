import email.parser

from .dict_serializer import DictSerializer
from .serializer import Serializer
import json

class FormSerializer(Serializer):
    def serialize(self, value: object) -> str:
        return None

    def deserialize(self, value: str, target_class: type, mime_type: str) -> object:
      dict_serializer = DictSerializer()

      deserialized_dict = {}
      for keyvalue_pair in value.splitlines():
        result = keyvalue_pair.split('=')
        deserialized_dict[result[0]] = result[1]

      return dict_serializer.deserialize(deserialized_dict, target_class)
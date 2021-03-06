from typing import List, Dict

from strawberry_py.parsers.serializer import Serializer
from strawberry_py.parsers.json_serializer import JsonSerializer
from strawberry_py.parsers.raw_serializer import RawSerializer
from strawberry_py.parsers.form_serializer import FormSerializer
from strawberry_py.parsers.multipart_serializer import MultipartSerializer
from strawberry_py.errors.server_error import ServerError

class ContentSerializerRegistry:
  _instance = None

  @staticmethod
  def get_instance() -> 'ContentSerializerRegistry':
    if ContentSerializerRegistry._instance is None:
      ContentSerializerRegistry._instance = ContentSerializerRegistry()
    return ContentSerializerRegistry._instance

  def __init__(self):
    super().__init__()
    self.registered_serializers: Dict[str, Serializer] = {
      'application/json': JsonSerializer(),
      'multipart/form-data': MultipartSerializer(),
      'application/x-www-form-urlencoded': FormSerializer(),
      'text/plain': RawSerializer()
    }

  def register_serializer(self, serializer: Serializer, *keys: List[str]) -> None:
    for key in keys:
      self.registered_serializers[key] = serializer

  def get_serializer(self, key: str) -> Serializer:
    key = self.clean_mimetype(key)
    return self.registered_serializers.get(key, None)

  def serialize(self, value: object, mime_type: str) -> object:
    if mime_type is None:
      raise Exception('ContentType Header not set or value not known')

    return self.get_serializer(mime_type).serialize(value)

  def deserialize(self, value: str, mime_type: str, target_type: type) -> object:
    if mime_type is None:
      raise Exception('ContentType Header not set or value not known')
    return self.get_serializer(mime_type).deserialize(value, target_type, mime_type)

  def clean_mimetype(self, mime_type: str):
    mime_type = mime_type[0:mime_type.find(';')]
    return mime_type
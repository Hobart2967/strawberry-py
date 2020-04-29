from .serializer import Serializer
from typing import List

class DictSerializer(Serializer):
  def serialize(self, source_object: object) -> dict:
      if source_object is None:
          return None

      if type(source_object) in (int, float, bool, str):
          return source_object

      if isinstance(source_object, list):
          return list(map(lambda item: self.serialize(item), source_object))

      serialization_infos = self.get_serialization_infos(type(source_object))
      target_dict = {}
      for info in serialization_infos:
          value = getattr(source_object, info.property_name)
          target_dict[info.serialized_name] = self.serialize(value)

      return target_dict

  def deserialize(self, source_dict: dict, target_class: type) -> object:
      target_obj = target_class()
      serialization_infos = self.get_serialization_infos(target_class)
      for info in serialization_infos:
          setattr(target_obj, info.property_name, source_dict[info.serialized_name])

      return target_obj
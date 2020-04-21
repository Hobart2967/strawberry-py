from .serializer import Serializer

class DictSerializer(Serializer):
  def serialize(self, source_object: object) -> dict:
      serialization_infos = self.get_serialization_infos(type(source_object))
      print(serialization_infos)
      target_dict = {}
      for info in serialization_infos:
          target_dict[info.serialized_name] = getattr(source_object, info.property_name)

      return target_dict

  def deserialize(self, source_dict: dict, target_class: type) -> object:
      target_obj = target_class()
      serialization_infos = self.get_serialization_infos(target_class)
      print(serialization_infos)
      for info in serialization_infos:
          setattr(target_obj, info.property_name, source_dict[info.serialized_name])

      return target_obj
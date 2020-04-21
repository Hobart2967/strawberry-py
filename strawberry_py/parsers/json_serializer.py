from .dict_serializer import DictSerializer
import json

class JsonSerializer(DictSerializer):
    def serialize(self, value: object) -> str:
        serialized_json_dict = super().serialize(value)
        return json.dumps(serialized_json_dict)

    def deserialize(self, value: str, target_class: type) -> object:
        deserialized_json_dict = json.loads(value)
        return super().deserialize(deserialized_json_dict, target_class)
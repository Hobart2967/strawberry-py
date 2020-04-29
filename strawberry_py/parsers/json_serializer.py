from .dict_serializer import DictSerializer
from .serializer import Serializer
import json

class JsonSerializer(Serializer):
    def serialize(self, value: object) -> str:
        dict_serializer = DictSerializer()
        serialized_json_dict = dict_serializer.serialize(value)
        return json.dumps(serialized_json_dict)

    def deserialize(self, value: str, target_class: type) -> object:
        dict_serializer = DictSerializer()
        deserialized_json_dict = json.loads(value)
        return dict_serializer.deserialize(deserialized_json_dict, target_class)
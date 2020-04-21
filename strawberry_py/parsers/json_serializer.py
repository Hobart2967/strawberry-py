from .dict_serializer import DictSerializer
import json

class JsonSerializer(DictSerializer):
    def serialize(self, value: object) -> str:
        dict_serializer = DictSerializer()
        serialized_json_dict = dict_serializer.serialize(value)
        print(serialized_json_dict)
        return json.dumps(serialized_json_dict)

    def deserialize(self, value: str, target_class: type) -> object:
        dict_serializer = DictSerializer()
        deserialized_json_dict = json.loads(value)
        return dict_serializer.deserialize(deserialized_json_dict, target_class)
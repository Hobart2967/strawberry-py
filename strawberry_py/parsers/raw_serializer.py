from .dict_serializer import DictSerializer
from .serializer import Serializer
import json

class RawSerializer(Serializer):
    def serialize(self, value: object) -> str:
        return value

    def deserialize(self, value: str, target_class: type) -> object:
        return value
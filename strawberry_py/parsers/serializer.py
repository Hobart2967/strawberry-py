from abc import ABCMeta, abstractmethod
import inspect
from strawberry_py.decorators.parsing.serialize import serialize
from typing import List
from strawberry_py.models.serialization_info import SerializationInfo

class Serializer(metaclass=ABCMeta):
    @abstractmethod
    def serialize(self, value: object) -> str:
        pass

    @abstractmethod
    def deserialize(self, value: str, target_class: type) -> object:
        pass

    def get_serialization_infos(self, klass: type) -> List[SerializationInfo]:
        serialization_infos = []
        print(klass)
        for name, member in inspect.getmembers(klass):
            if name == "id":
              print(getattr(getattr(getattr(klass, name), 'fget'), serialize.name))
            if not hasattr(member, 'fget') or not hasattr(getattr(member, 'fget'), serialize.name):
                continue
            serialization_infos.append(getattr(getattr(member, 'fget'), serialize.name))

        return serialization_infos
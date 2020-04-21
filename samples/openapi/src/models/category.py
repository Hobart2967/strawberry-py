# This is a sample model mustache template.
from strawberry_py import Model, serialize


class Category(Model):
    def __init__(self, id: int=None, name: str=None):
      self._id = id
      self._name = name

    @property
    @serialize('id', int)
    def id(self):
      return self._id

    @id.setter
    def id(self, value: int):
      self._id = value


    @property
    @serialize('name', str)
    def name(self):
      return self._name

    @name.setter
    def name(self, value: str):
      self._name = value



# This is a sample model mustache template.
from strawberry_py import Model


class Tag(Model):
     def __init__(self, id: int=None, name: str=None):
      self._id = id
      self._name = name

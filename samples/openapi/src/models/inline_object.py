# This is a sample model mustache template.
from strawberry_py import Model


class InlineObject(Model):
     def __init__(self, name: str=None, status: str=None):
      self._name = name
      self._status = status

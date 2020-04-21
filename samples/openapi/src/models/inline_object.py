# This is a sample model mustache template.
from strawberry_py import Model, serialize


class InlineObject(Model):
    def __init__(self, name: str=None, status: str=None):
      self._name = name
      self._status = status

    @property
    @serialize('name', str)
    def name(self):
      return self._name

    @name.setter
    def name(self, value: str):
      self._name = value


    @property
    @serialize('status', str)
    def status(self):
      return self._status

    @status.setter
    def status(self, value: str):
      self._status = value



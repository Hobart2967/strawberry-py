# This is a sample model mustache template.
from strawberry_py import Model, serialize


class ApiResponse(Model):
    def __init__(self, code: int=None, type: str=None, message: str=None):
      self._code = code
      self._type = type
      self._message = message

    @property
    @serialize('code', int)
    def code(self):
      return self._code

    @code.setter
    def code(self, value: int):
      self._code = value


    @property
    @serialize('type', str)
    def type(self):
      return self._type

    @type.setter
    def type(self, value: str):
      self._type = value


    @property
    @serialize('message', str)
    def message(self):
      return self._message

    @message.setter
    def message(self, value: str):
      self._message = value



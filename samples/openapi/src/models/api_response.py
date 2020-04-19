# This is a sample model mustache template.
from strawberry_py import Model


class ApiResponse(Model):
     def __init__(self, code: int=None, type: str=None, message: str=None):
      self._code = code
      self._type = type
      self._message = message

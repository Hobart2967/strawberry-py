# This is a sample model mustache template.
from strawberry_py import Model


class InlineObject1(Model):
     def __init__(self, additional_metadata: str=None, file: file=None):
      self._additional_metadata = additional_metadata
      self._file = file

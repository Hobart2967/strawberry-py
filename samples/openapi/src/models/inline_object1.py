# This is a sample model mustache template.
from strawberry_py import Model, serialize


class InlineObject1(Model):
    def __init__(self, additional_metadata: str=None, file: 'file'=None):
      self._additional_metadata = additional_metadata
      self._file = file

    @property
    @serialize('additional_metadata', str)
    def additional_metadata(self):
      return self._additional_metadata

    @additional_metadata.setter
    def additional_metadata(self, value: str):
      self._additional_metadata = value


    @property
    @serialize('file', 'file')
    def file(self):
      return self._file

    @file.setter
    def file(self, value: 'file'):
      self._file = value



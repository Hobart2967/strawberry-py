# This is a sample model mustache template.
from strawberry_py import Model, serialize
from typing import *


class InlineObject1(Model):
    def __init__(self, additional_metadata: str=None, file: str=None):
      self._additional_metadata = additional_metadata
      self._file = file

    @property
    @serialize('additionalMetadata', str)
    def additional_metadata(self):
      return self._additional_metadata

    @additional_metadata.setter
    def additional_metadata(self, value: str):
      self._additional_metadata = value


    @property
    @serialize('file', str)
    def file(self):
      return self._file

    @file.setter
    def file(self, value: str):
      self._file = value



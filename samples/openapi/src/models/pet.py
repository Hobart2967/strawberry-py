# This is a sample model mustache template.
from strawberry_py import Model, serialize
from typing import *

from src.models.category import *
from src.models.tag import *

class Pet(Model):
    def __init__(self, id: int=None, category: Category=None, name: str=None, photo_urls: List[str]=None, tags: List[Tag]=None, status: str=None):
      self._id = id
      self._category = category
      self._name = name
      self._photo_urls = photo_urls
      self._tags = tags
      self._status = status

    @property
    @serialize('id', int)
    def id(self):
      return self._id

    @id.setter
    def id(self, value: int):
      self._id = value


    @property
    @serialize('category', Category)
    def category(self):
      return self._category

    @category.setter
    def category(self, value: Category):
      self._category = value


    @property
    @serialize('name', str)
    def name(self):
      return self._name

    @name.setter
    def name(self, value: str):
      self._name = value


    @property
    @serialize('photoUrls', List[str])
    def photo_urls(self):
      return self._photo_urls

    @photo_urls.setter
    def photo_urls(self, value: List[str]):
      self._photo_urls = value


    @property
    @serialize('tags', List[Tag])
    def tags(self):
      return self._tags

    @tags.setter
    def tags(self, value: List[Tag]):
      self._tags = value


    @property
    @serialize('status', str)
    def status(self):
      return self._status

    @status.setter
    def status(self, value: str):
      self._status = value



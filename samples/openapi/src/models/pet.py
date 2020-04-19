# This is a sample model mustache template.
from strawberry_py import Model

from src.models.category import *
from src.models.tag import *

class Pet(Model):
     def __init__(self, id: int=None, category: Category=None, name: str=None, photo_urls: list=None, tags: list=None, status: str=None):
      self._id = id
      self._category = category
      self._name = name
      self._photo_urls = photo_urls
      self._tags = tags
      self._status = status

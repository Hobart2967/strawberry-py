# This is a sample model mustache template.
from strawberry_py import Model

from datetime import *

class Order(Model):
     def __init__(self, id: int=None, pet_id: int=None, quantity: int=None, ship_date: date=None, status: str=None, complete: bool=False):
      self._id = id
      self._pet_id = pet_id
      self._quantity = quantity
      self._ship_date = ship_date
      self._status = status
      self._complete = complete

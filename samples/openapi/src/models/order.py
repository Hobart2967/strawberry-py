# This is a sample model mustache template.
from strawberry_py import Model, serialize
from typing import *

from datetime import *

class Order(Model):
    def __init__(self, id: int=None, pet_id: int=None, quantity: int=None, ship_date: date=None, status: str=None, complete: bool=False):
      self._id = id
      self._pet_id = pet_id
      self._quantity = quantity
      self._ship_date = ship_date
      self._status = status
      self._complete = complete

    @property
    @serialize('id', int)
    def id(self):
      return self._id

    @id.setter
    def id(self, value: int):
      self._id = value


    @property
    @serialize('pet_id', int)
    def pet_id(self):
      return self._pet_id

    @pet_id.setter
    def pet_id(self, value: int):
      self._pet_id = value


    @property
    @serialize('quantity', int)
    def quantity(self):
      return self._quantity

    @quantity.setter
    def quantity(self, value: int):
      self._quantity = value


    @property
    @serialize('ship_date', date)
    def ship_date(self):
      return self._ship_date

    @ship_date.setter
    def ship_date(self, value: date):
      self._ship_date = value


    @property
    @serialize('status', str)
    def status(self):
      return self._status

    @status.setter
    def status(self, value: str):
      self._status = value


    @property
    @serialize('complete', bool)
    def complete(self):
      return self._complete

    @complete.setter
    def complete(self, value: bool):
      self._complete = value



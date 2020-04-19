# This is a sample model mustache template.
from strawberry_py import Model


class User(Model):
     def __init__(self, id: int=None, username: str=None, first_name: str=None, last_name: str=None, email: str=None, password: str=None, phone: str=None, user_status: int=None):
      self._id = id
      self._username = username
      self._first_name = first_name
      self._last_name = last_name
      self._email = email
      self._password = password
      self._phone = phone
      self._user_status = user_status

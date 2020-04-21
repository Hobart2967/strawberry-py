# This is a sample model mustache template.
from strawberry_py import Model, serialize
from typing import *


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

    @property
    @serialize('id', int)
    def id(self):
      return self._id

    @id.setter
    def id(self, value: int):
      self._id = value


    @property
    @serialize('username', str)
    def username(self):
      return self._username

    @username.setter
    def username(self, value: str):
      self._username = value


    @property
    @serialize('firstName', str)
    def first_name(self):
      return self._first_name

    @first_name.setter
    def first_name(self, value: str):
      self._first_name = value


    @property
    @serialize('lastName', str)
    def last_name(self):
      return self._last_name

    @last_name.setter
    def last_name(self, value: str):
      self._last_name = value


    @property
    @serialize('email', str)
    def email(self):
      return self._email

    @email.setter
    def email(self, value: str):
      self._email = value


    @property
    @serialize('password', str)
    def password(self):
      return self._password

    @password.setter
    def password(self, value: str):
      self._password = value


    @property
    @serialize('phone', str)
    def phone(self):
      return self._phone

    @phone.setter
    def phone(self, value: str):
      self._phone = value


    @property
    @serialize('userStatus', int)
    def user_status(self):
      return self._user_status

    @user_status.setter
    def user_status(self, value: int):
      self._user_status = value



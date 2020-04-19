from strawberry_py import ApiController, http_get, http_put, http_post, http_patch, http_delete, form_parameter, body_parameter, query_string_parameter, header_parameter
from abc import ABCMeta, abstractmethod

from src.models.user import *

class UserApiController(ApiController, metaclass=ABCMeta):

  @http_post('/v2/user')
  @body_parameter('user', required=True)
  @abstractmethod
  def create_user(self, user: user) -> None:
    return None

  @http_post('/v2/user/createWithArray')
  @body_parameter('user', required=True)
  @abstractmethod
  def create_users_with_array_input(self, user: list) -> None:
    return None

  @http_post('/v2/user/createWithList')
  @body_parameter('user', required=True)
  @abstractmethod
  def create_users_with_list_input(self, user: list) -> None:
    return None

  @http_delete('/v2/user/{username}')
  @abstractmethod
  def delete_user(self, username: str) -> None:
    return None

  @http_get('/v2/user/{username}')
  @abstractmethod
  def get_user_by_name(self, username: str) -> User:
    return None

  @http_get('/v2/user/login')
  @query_string_parameter('username', required=True)
  @query_string_parameter('password', required=True)
  @abstractmethod
  def login_user(self, username: str, password: str) -> String:
    return None

  @http_get('/v2/user/logout')
  @abstractmethod
  def logout_user(self) -> None:
    return None

  @http_put('/v2/user/{username}')
  @body_parameter('user', required=True)
  @abstractmethod
  def update_user(self, username: str, user: user) -> None:
    return None


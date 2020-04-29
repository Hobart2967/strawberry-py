from strawberry_py import ApiController, http_get, http_put, http_post, http_patch, http_delete, form_parameter, body_parameter, query_string_parameter, header_parameter, path_parameter
from abc import ABCMeta, abstractmethod
from typing import *

from src.models.user import *

class UserApiController(ApiController, metaclass=ABCMeta):

  @http_post('/v2/user')
  @body_parameter('user', data_type=User, required=True)
  @abstractmethod
  def create_user(self, user: User) -> None:
    return None

  @http_post('/v2/user/createWithArray')
  @body_parameter('user', data_type=List[User], required=True)
  @abstractmethod
  def create_users_with_array_input(self, user: List[User]) -> None:
    return None

  @http_post('/v2/user/createWithList')
  @body_parameter('user', data_type=List[User], required=True)
  @abstractmethod
  def create_users_with_list_input(self, user: List[User]) -> None:
    return None

  @http_delete('/v2/user/{username}')
  @path_parameter('username', data_type=str, required=True)
  @abstractmethod
  def delete_user(self, username: str) -> None:
    return None

  @http_get('/v2/user/{username}')
  @path_parameter('username', data_type=str, required=True)
  @abstractmethod
  def get_user_by_name(self, username: str) -> User:
    return None

  @http_get('/v2/user/login')
  @query_string_parameter('username', data_type=str, required=True)
  @query_string_parameter('password', data_type=str, required=True)
  @abstractmethod
  def login_user(self, username: str, password: str) -> str:
    return None

  @http_get('/v2/user/logout')
  @abstractmethod
  def logout_user(self) -> None:
    return None

  @http_put('/v2/user/{username}')
  @path_parameter('username', data_type=str, required=True)
  @body_parameter('user', data_type=User, required=True)
  @abstractmethod
  def update_user(self, username: str, user: User) -> None:
    return None


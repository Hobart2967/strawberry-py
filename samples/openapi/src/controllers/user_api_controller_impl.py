from strawberry_py import controller
from src.controllers.user_api_controller import UserApiController

@controller(UserApiController)
class UserApiControllerImpl(UserApiController):

  def create_user(self, user: user) -> None:
    super().create_user(user)
    raise NotImplementedError

  def create_users_with_array_input(self, user: list) -> None:
    super().create_users_with_array_input(user)
    raise NotImplementedError

  def create_users_with_list_input(self, user: list) -> None:
    super().create_users_with_list_input(user)
    raise NotImplementedError

  def delete_user(self, username: str) -> None:
    super().delete_user(username)
    raise NotImplementedError

  def get_user_by_name(self, username: str) -> User:
    super().get_user_by_name(username)
    raise NotImplementedError

  def login_user(self, username: str, password: str) -> String:
    super().login_user(username, password)
    raise NotImplementedError

  def logout_user(self) -> None:
    super().logout_user()
    raise NotImplementedError

  def update_user(self, username: str, user: user) -> None:
    super().update_user(username, user)
    raise NotImplementedError


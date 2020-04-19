from strawberry_py import controller
from src.controllers.pet_api_controller import PetApiController

@controller(PetApiController)
class PetApiControllerImpl(PetApiController):

  def add_pet(self, pet: pet) -> None:
    super().add_pet(pet)
    raise NotImplementedError

  def delete_pet(self, pet_id: int, api_key: str=None) -> None:
    super().delete_pet(pet_id, api_key)
    raise NotImplementedError

  def find_pets_by_status(self, status: list) -> List:
    super().find_pets_by_status(status)
    raise NotImplementedError

  def find_pets_by_tags(self, tags: list) -> List:
    super().find_pets_by_tags(tags)
    raise NotImplementedError

  def get_pet_by_id(self, pet_id: int) -> Pet:
    super().get_pet_by_id(pet_id)
    raise NotImplementedError

  def update_pet(self, pet: pet) -> None:
    super().update_pet(pet)
    raise NotImplementedError

  def update_pet_with_form(self, pet_id: int, name: str=None, status: str=None) -> None:
    super().update_pet_with_form(pet_id, name, status)
    raise NotImplementedError

  def upload_file(self, pet_id: int, additional_metadata: str=None, file: file=None) -> ApiResponse:
    super().upload_file(pet_id, additional_metadata, file)
    raise NotImplementedError


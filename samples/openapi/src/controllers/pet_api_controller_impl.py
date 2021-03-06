from strawberry_py import controller, header_parameter, query_string_parameter

from src.controllers.pet_api_controller import PetApiController

from src.models.api_response import *
from src.models.pet import *
from src.models.tag import *

@controller(PetApiController)
class PetApiControllerImpl(PetApiController):

  def add_pet(self, pet: Pet) -> None:
    super().add_pet(pet)
    raise NotImplementedError

  def delete_pet(self, pet_id: int, api_key: str=None) -> None:
    super().delete_pet(pet_id, api_key)
    raise NotImplementedError

  def find_pets_by_status(self, status: list) -> list:
    super().find_pets_by_status(status)
    raise NotImplementedError

  def find_pets_by_tags(self, tags: str) -> list:
    super().find_pets_by_tags(tags)
    raise NotImplementedError

  @header_parameter('apiKey', data_type=str, required=True, minimum_length=1, maximum_length=2, pattern='[0-9]+')
  @query_string_parameter('TestKey', data_type=List[int])
  def get_pet_by_id(self, pet_id: int, api_key: str, test_key: List[str]) -> Pet:
    print(test_key)
    return Pet(
      id=pet_id,
      tags=[
        Tag(id=1, name="Golden Retriever"),
        Tag(id=2, name="Golden")
      ],
      status=api_key)

  def update_pet(self, pet: Pet) -> None:
    super().update_pet(pet)
    raise NotImplementedError

  def update_pet_with_form(self, pet_id: int, name: str=None, status: str=None) -> None:
    super().update_pet_with_form(pet_id, name, status)
    raise NotImplementedError

  def upload_file(self, pet_id: int, additional_metadata: str=None, file: 'file'=None) -> ApiResponse:
    super().upload_file(pet_id, additional_metadata, file)
    raise NotImplementedError


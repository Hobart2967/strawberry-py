from strawberry_py import ApiController, http_get, http_put, http_post, http_patch, http_delete, form_parameter, body_parameter, query_string_parameter, header_parameter
from abc import ABCMeta, abstractmethod

from src.models.api_response import *
from src.models.pet import *

class PetApiController(ApiController, metaclass=ABCMeta):

  @http_post('/v2/pet')
  @body_parameter('pet', required=True)
  @abstractmethod
  def add_pet(self, pet: pet) -> None:
    return None

  @http_delete('/v2/pet/{petId}')
  @header_parameter('api_key')
  @abstractmethod
  def delete_pet(self, pet_id: int, api_key: str=None) -> None:
    return None

  @http_get('/v2/pet/findByStatus')
  @query_string_parameter('status', required=True)
  @abstractmethod
  def find_pets_by_status(self, status: list) -> List:
    return None

  @http_get('/v2/pet/findByTags')
  @query_string_parameter('tags', required=True)
  @abstractmethod
  def find_pets_by_tags(self, tags: list) -> List:
    return None

  @http_get('/v2/pet/{petId}')
  @abstractmethod
  def get_pet_by_id(self, pet_id: int) -> Pet:
    return None

  @http_put('/v2/pet')
  @body_parameter('pet', required=True)
  @abstractmethod
  def update_pet(self, pet: pet) -> None:
    return None

  @http_post('/v2/pet/{petId}')
  @form_parameter('name')
  @form_parameter('status')
  @abstractmethod
  def update_pet_with_form(self, pet_id: int, name: str=None, status: str=None) -> None:
    return None

  @http_post('/v2/pet/{petId}/uploadImage')
  @form_parameter('additional_metadata')
  @form_parameter('file')
  @abstractmethod
  def upload_file(self, pet_id: int, additional_metadata: str=None, file: file=None) -> ApiResponse:
    return None


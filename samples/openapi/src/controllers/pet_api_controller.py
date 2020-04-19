from strawberry_py import ApiController, http_get, http_put, http_post, http_patch, http_delete, form_parameter, body_parameter, query_string_parameter, header_parameter, path_parameter
from abc import ABCMeta, abstractmethod

from src.models.api_response import *
from src.models.pet import *

class PetApiController(ApiController, metaclass=ABCMeta):

  @http_post('/v2/pet')
  @body_parameter('pet', type=Pet, required=True)
  @abstractmethod
  def add_pet(self, pet: Pet) -> None:
    return None

  @http_delete('/v2/pet/{petId}')
  @path_parameter('petId', type=int, required=True)
  @header_parameter('apiKey', type=str)
  @abstractmethod
  def delete_pet(self, pet_id: int, api_key: str=None) -> None:
    return None

  @http_get('/v2/pet/findByStatus')
  @query_string_parameter('status', type=list, required=True)
  @abstractmethod
  def find_pets_by_status(self, status: list) -> list:
    return None

  @http_get('/v2/pet/findByTags')
  @query_string_parameter('tags', type=list, required=True)
  @abstractmethod
  def find_pets_by_tags(self, tags: list) -> list:
    return None

  @http_get('/v2/pet/{petId}')
  @path_parameter('petId', type=int, required=True)
  @abstractmethod
  def get_pet_by_id(self, pet_id: int) -> Pet:
    return None

  @http_put('/v2/pet')
  @body_parameter('pet', type=Pet, required=True)
  @abstractmethod
  def update_pet(self, pet: Pet) -> None:
    return None

  @http_post('/v2/pet/{petId}')
  @path_parameter('petId', type=int, required=True)
  @form_parameter('name', type=str)
  @form_parameter('status', type=str)
  @abstractmethod
  def update_pet_with_form(self, pet_id: int, name: str=None, status: str=None) -> None:
    return None

  @http_post('/v2/pet/{petId}/uploadImage')
  @path_parameter('petId', type=int, required=True)
  @form_parameter('additionalMetadata', type=str)
  @form_parameter('file', type='file')
  @abstractmethod
  def upload_file(self, pet_id: int, additional_metadata: str=None, file: 'file'=None) -> ApiResponse:
    return None


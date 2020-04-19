from strawberry_py import ApiController, http_get, http_put, http_post, http_patch, http_delete, form_parameter, body_parameter, query_string_parameter, header_parameter
from abc import ABCMeta, abstractmethod

from src.models.order import *

class StoreApiController(ApiController, metaclass=ABCMeta):

  @http_delete('/v2/store/order/{orderId}')
  @abstractmethod
  def delete_order(self, order_id: str) -> None:
    return None

  @http_get('/v2/store/inventory')
  @abstractmethod
  def get_inventory(self) -> dict:
    return None

  @http_get('/v2/store/order/{orderId}')
  @abstractmethod
  def get_order_by_id(self, order_id: int) -> Order:
    return None

  @http_post('/v2/store/order')
  @body_parameter('order', required=True)
  @abstractmethod
  def place_order(self, order: Order) -> Order:
    return None


from strawberry_py import controller
from src.controllers.store_api_controller import StoreApiController

from src.models.order import *


@controller(StoreApiController)
class StoreApiControllerImpl(StoreApiController):

  def delete_order(self, order_id: str) -> None:
    super().delete_order(order_id)
    raise NotImplementedError

  def get_inventory(self) -> dict:
    super().get_inventory()
    raise NotImplementedError

  def get_order_by_id(self, order_id: int) -> Order:
    super().get_order_by_id(order_id)
    raise NotImplementedError

  def place_order(self, order: Order) -> Order:
    super().place_order(order)
    raise NotImplementedError


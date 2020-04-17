import inspect
from services.controller_handler import ControllerHandler
from functools import wraps

def http_get(path):
  def decorator(func):
    ControllerHandler.get_instance().registerEndpoint(func, {
      'method': 'GET',
      'path': path
    })
    return func
  return decorator
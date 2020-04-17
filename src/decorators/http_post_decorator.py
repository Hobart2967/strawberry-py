import inspect
from services.controller_handler import ControllerHandler
from functools import wraps

def http_post(path, body):
  def decorator(func):
    ControllerHandler.get_instance().registerEndpoint(func, {
      'method': 'POST',
      'path': path,
      'body_arg': body
    })
    return func
  return decorator
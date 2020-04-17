from collections import namedtuple

def dict_to_object(d):
  for k,v in d.items():
    if isinstance(v, dict):
      d[k] = dict_to_object(v)
  return namedtuple('object', d.keys())(*d.values())
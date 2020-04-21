def serialize(name, type):
  def decorator(property_getter):
    return property_getter
  return decorator
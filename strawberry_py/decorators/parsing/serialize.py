from strawberry_py.models.serialization_info import SerializationInfo

def serialize(serialized_name, serialized_type):
  def decorator(property_getter):
    if not callable(property_getter):
        property_getter_function = property_getter.fget
    else:
        property_getter_function = property_getter

    property_getter_function.serialize_info = SerializationInfo(
      serialized_name=serialized_name,
      serialized_type=serialized_type,
      property_name=property_getter_function.__name__)

    return property_getter
  return decorator

serialize.name = 'serialize_info'
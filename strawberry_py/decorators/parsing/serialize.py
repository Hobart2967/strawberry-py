from strawberry_py.models.serialization_info import SerializationInfo

def serialize(serialized_name, serialized_type):
  def decorator(property_getter):
    if not callable(property_getter):
        print('Setting info on propgetter ', property_getter.fget)
        property_getter_function = property_getter.fget
    else:
        print('Setting info on direct function ', property_getter)
        property_getter_function = property_getter

    property_getter_function.serialize_info = SerializationInfo(
      serialized_name=serialized_name,
      serialized_type=serialized_type,
      property_name=property_getter_function.__name__)

    # print(getattr(getattr(klass, 'person_name'), 'fget').serialize_info)
    return property_getter
  return decorator

serialize.name = 'serialize_info'
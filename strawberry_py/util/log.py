class Log:
  debug_handler = lambda *message_segments: Log.debug_default(*message_segments)
  @staticmethod
  def debug(*message_segments: str):
    Log.debug_handler(*message_segments)

  @staticmethod
  def debug_default(*message_segments: str):
    print('[DEBUG]', *message_segments)
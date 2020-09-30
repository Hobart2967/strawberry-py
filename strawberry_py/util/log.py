from typing import List

class LogLevel:
  TRACE = 10
  DEBUG = 20
  INFO = 30
  WARN = 40
  ERROR = 50

class Log:
  log_level = LogLevel.INFO

  debug_handler = lambda *message_segments: Log.debug_default(*message_segments)
  @staticmethod
  def debug(*message_segments: str):
    Log.debug_handler(*message_segments)

  @staticmethod
  def debug_default(*message_segments: List[str]):
    if Log.log_level <= LogLevel.DEBUG:
      print('[DEBUG]', ' '.join(message_segments))

  info_handler = lambda *message_segments: Log.info_default(*message_segments)
  @staticmethod
  def info(*message_segments: str):
    Log.info_handler(*message_segments)

  @staticmethod
  def info_default(*message_segments: List[str]):
    if Log.log_level <= LogLevel.INFO:
      print('[INFO]', ' '.join(message_segments), '"')
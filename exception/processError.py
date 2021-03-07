import logging

class ProcessError(Exception):
  def __init__(self, msg):
    Exception.__init__(self, msg)
    self._msg = msg

    logging.error(f'{msg}')
import logging

class ScrappingError(Exception):
  def __init__(self, msg):
    Exception.__init__(self, msg)
    self._msg = msg

    logging.warning(f'{msg}')

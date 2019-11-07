class Error(Exception):
  '''Base class for other exceptions'''
  pass

class LinkNotFound(Error):
  '''Raised when the link return invalid values'''
  def __init__(self, msg):
    Error.__init__(self, msg)
    self._msg = msg

class ValueNotFound(Error):
  '''Raised when the process of extract return invalid value '''
  def __init__(self, msg):
    Error.__init__(self, msg)
    self._msg = msg
    

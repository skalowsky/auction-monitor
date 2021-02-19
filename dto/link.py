class Link:
  
  def __init__(self):
    self.url: str
    self.address: str
    self.district:str
    self.city: str
    self.state: str

  def __str__(self) -> str:
    # return 'self.url'
    return self.url

  def __validLink__(self) -> bool:
    return hasattr(self, 'link')
    # return True
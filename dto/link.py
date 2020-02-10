class Link:
  
  def __init__(self):
    self.link: str
    self.address: str
    self.district:str
    self.city: str
    self.state: str

  def __str__(self) -> str:
    return self.link

  def __validLink__(self) -> bool:
    return hasattr(self, 'link')
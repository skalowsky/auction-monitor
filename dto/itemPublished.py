import datetime
from dto.link import Link

class ItemPublished:

  def __init__(self):
    self.id: str
    self.link: Link
    self.generalAddress: str
    self.appraisalValue: float
    self.appraisalMinimumValue: float
    self.appraisalBetterValue: float
    self.description: str
    self.typeProperty: str
    self.numberOfRoom: int
    self.garage: str
    self.situation: str
    self.totalArea: float
    self.privateArea: float
    self.landArea: float
    self.additionalInformation: str
    self.timeRemainingOnline: datetime

  

  def __str__(self):
    return f'id: {self.id}, address: {self.generalAddress} '





# BCFF11 - FII BC FFII
# HGLG11
# KNRJ11
# BIDI4
# ITSA4
# FLRY3
# ALZR11
# ARZZ3
# BIDI11

# JHCF11

#TREND DI SIMPLE -> fundo que investe em crédito privado
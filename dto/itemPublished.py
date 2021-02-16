from dto.link import Link

from enums.typeProperty import TypeProperty
from enums.situation import Situation

from util.json import Encoder

class ItemPublished:

  def __init__(self):
    self.id: str
    self.companyId: int
    self.link: Link
    self.generalAddress: str
    self.appraisalValue: float
    self.appraisalMinimumValue: float
    self.appraisalBetterValue: float
    self.description: str
    self.typeProperty: TypeProperty
    self.numberOfRoom: int
    self.garage: str
    self.situation: Situation
    self.totalArea: float
    self.privateArea: float
    self.landArea: float
    self.additionalInformation: str
    self.auctionDate: str

  def __json__(self):
    return Encoder().__json__(self)

  def __str__(self):
    return f'id: {self.id}, address: {self.generalAddress} '


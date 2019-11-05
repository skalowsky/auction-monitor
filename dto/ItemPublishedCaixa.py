class ItemPublishedCaixa:

  def __init__(self):
    self.address = None
    self.appraisalValue = None
    self.appraisalMinimumValue = None
    self.auctionBid = None
    self.description = None
    self.typeImmobile = None
    self.numberOfRoom = None
    self.situation = None
    self.totalArea = None
    self.privateArea = None
    self.additionalInformation = None
    self.timeRemainingOnline = None

  @property
  def address(self):
    return self._address
  
  @address.setter
  def address(self, address):
    self._address = address

  @property
  def appraisalValue(self):
    return self.appraisalValue
  
  @appraisalValue.setter
  def appraisalValue(self, appraisalValue):
    self.appraisalValue = appraisalValue

  @property
  def appraisalMinimumValue(self):
    return self.appraisalMinimumValue
  
  @appraisalMinimumValue.setter
  def appraisalMinimumValue(self, appraisalMinimumValue):
    self.appraisalMinimumValue = appraisalMinimumValue

  @property
  def description(self):
    return self.description
  
  @description.setter
  def description(self, description):
    self.description = description

  @property
  def typeImmobile(self):
    return self.typeImmobile
  
  @typeImmobile.setter
  def typeImmobile(self, typeImmobile):
    self.typeImmobile = typeImmobile      

  @property
  def numberOfRoom(self):
    return self.numberOfRoom
  
  @numberOfRoom.setter
  def numberOfRoom(self, numberOfRoom):
    self.numberOfRoom = numberOfRoom 

  @property
  def situation(self):
    return self.situation
  
  @situation.setter
  def situation(self, situation):
    self.situation = situation 

  @property
  def totalArea(self):
    return self.totalArea
  
  @totalArea.setter
  def totalArea(self, totalArea):
    self.totalArea = totalArea 

  @property
  def privateArea(self):
    return self.privateArea
  
  @privateArea.setter
  def privateArea(self, privateArea):
    self.privateArea = privateArea 

  @property
  def additionalInformation(self):
    return self.additionalInformation
  
  @additionalInformation.setter
  def additionalInformation(self, additionalInformation):
    self.additionalInformation = additionalInformation 

  @property
  def auctionBid(self):
    return self.auctionBid
  
  @auctionBid.setter
  def auctionBid(self, auctionBid):
    self.auctionBid = auctionBid 

  @property
  def timeRemainingOnline(self):
    return self.timeRemainingOnline
  
  @timeRemainingOnline.setter
  def timeRemainingOnline(self, timeRemainingOnline):
    self.timeRemainingOnline = timeRemainingOnline 

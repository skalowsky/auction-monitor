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
    return self._appraisalValue
  
  @appraisalValue.setter
  def appraisalValue(self, appraisalValue):
    self._appraisalValue = appraisalValue

  @property
  def appraisalMinimumValue(self):
    return self._appraisalMinimumValue
  
  @appraisalMinimumValue.setter
  def appraisalMinimumValue(self, appraisalMinimumValue):
    self._appraisalMinimumValue = appraisalMinimumValue

  @property
  def description(self):
    return self._description
  
  @description.setter
  def description(self, description):
    self._description = description

  @property
  def typeImmobile(self):
    return self._typeImmobile
  
  @typeImmobile.setter
  def typeImmobile(self, typeImmobile):
    self._typeImmobile = typeImmobile      

  @property
  def numberOfRoom(self):
    return self._numberOfRoom
  
  @numberOfRoom.setter
  def numberOfRoom(self, numberOfRoom):
    self._numberOfRoom = numberOfRoom 

  @property
  def situation(self):
    return self._situation
  
  @situation.setter
  def situation(self, situation):
    self._situation = situation 

  @property
  def totalArea(self):
    return self._totalArea
  
  @totalArea.setter
  def totalArea(self, totalArea):
    self._totalArea = totalArea 

  @property
  def privateArea(self):
    return self._privateArea
  
  @privateArea.setter
  def privateArea(self, privateArea):
    self._privateArea = privateArea 

  @property
  def additionalInformation(self):
    return self._additionalInformation
  
  @additionalInformation.setter
  def additionalInformation(self, additionalInformation):
    self._additionalInformation = additionalInformation 

  @property
  def auctionBid(self):
    return self._auctionBid
  
  @auctionBid.setter
  def auctionBid(self, auctionBid):
    self._auctionBid = auctionBid 

  @property
  def timeRemainingOnline(self):
    return self._timeRemainingOnline
  
  @timeRemainingOnline.setter
  def timeRemainingOnline(self, timeRemainingOnline):
    self._timeRemainingOnline = timeRemainingOnline 


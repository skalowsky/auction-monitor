import logging

import requests
from requests.exceptions import MissingSchema

from bs4 import BeautifulSoup, ResultSet

from exception.linkNotFound import LinkNotFound

from dto.itemPublished import ItemPublished
from dto.link import Link

ERRO_TAG = "Ocorreu um erro durante o processamento de sua solicitação."

def getPageByLink(link: Link) -> BeautifulSoup:
  """This function gets all information by a received link 
  
  Arguments:
      link {Link} -- A link instances with a valid string link into a link property 
  
  Raises:
      LinkNotFound: A link instances with a null string link.
      LinkNotFound: A link instances with an invalid response. An invalid response contains the constant ERRO_TAG.
  
  Returns:
      BeautifulSoup -- A third party library that convert a string into a soap. 
  """  
  if not link or not link.link:
    raise LinkNotFound('Link received is null.')

  page = requests.get(link.link, verify=False)
  soup = BeautifulSoup(page.text, 'html.parser')    

  if ERRO_TAG in soup.currentTag.text:
    raise LinkNotFound(f'The link´s response is invalid - {link.link}')

  return soup


def extractInformationsByLink(link: Link) -> ItemPublished:
  """This function extracts all worth values from a valid link. 
  
  Arguments:
      link {Link} -- A link instances with a valid string link into a link property. 
  
  Returns:
      ItemPublished -- A class with all values extracted.
  """  

  itemPublished: ItemPublished = ItemPublished()

  logging.info(f'extracting information of link: {link.link}')

  try:
    soupPage = getPageByLink(link)

    setIdAndLink(itemPublished, link)
    setAddress(itemPublished, soupPage)
    setAppraisalValue(itemPublished, soupPage)
    setAppraisalMinimumValue(itemPublished, soupPage)
    setAppraisalBetterValue(itemPublished, soupPage)
    setDescription(itemPublished, soupPage)
    setTypeProperty(itemPublished, soupPage)
    setNumberOfRoom(itemPublished, soupPage)
    setSituation(itemPublished, soupPage)
    setGarage(itemPublished, soupPage)

    setTotalArea(itemPublished, soupPage)
    setPrivateArea(itemPublished, soupPage)
    setLandArea(itemPublished, soupPage)
    #setAdditionalInformation(itemPublished, soupPage)
    #setTimeRemainingOnline(itemPublished, soupPage)

    print (itemPublished.__str__())
  except Exception as e: 
    print (str(e))   
    itemPublished = ItemPublished()
  finally:
    return itemPublished


def existValidContent(item, index: int, messageError: str) -> bool:
  """This function verifies the consistency of the item extracted from soup.
  
  Arguments:
      item {[any]} -- The value to be tested.
      index {[int]} -- In array structure case, the index of the item to be tested.
      messageError {[str]} -- The message to be printed on log.
  Returns:
      [bool] -- In valid item ( [index] ) case, return true, else, return false, logging the message.
  """  

  try:
    if type(item) == ResultSet:
      return item[index] != None
    else:
      return item != None

  except:
    logging.warning(messageError)
    return False

def setIdAndLink(itemPublished: ItemPublished, link: Link):
  """This function extract the id and description from link.
  
  Arguments:
      itemPublished {ItemPublished} -- The carrier-class of property published.
      link {Link} -- A link instances with a valid string link into a link property.
  """  
  itemPublished.id = link.link.split('=')[-1]
  itemPublished.link = link

def setAddress(itemPublished: ItemPublished, soupPage: BeautifulSoup):
  """This function extract de general address. The value of the address, on soup, is an append of all address information, such as street, number, city, state, ...
  
  Arguments:
      itemPublished {ItemPublished} -- The carrier-class of property published.
      soupPage {BeautifulSoup} -- A third party library that contains all tags html in soup format.
  """  
  address = soupPage.find_all('p', attrs={'style': 'margin-bottom: 0.5em;'})

  if existValidContent(address, 0, f'id {itemPublished.id}. Address not found.') :
    itemPublished.generalAddress = address[0].text.replace('Endereço:', '')

def setAppraisalValue(itemPublished: ItemPublished, soupPage: BeautifulSoup):
  appraisalValue = soupPage.find('div', attrs={'class': 'content'}).find('p')
  value = appraisalValue.text.split(':')[1].replace(' R$ ', '').replace('Valor mínimo de venda','')

  if existValidContent(value, 0, f'id {itemPublished.id}. Appraisal Value not found.') :
    itemPublished.appraisalValue = value

def setAppraisalMinimumValue(itemPublished, soupPage):
  appraisalMinimumValue = soupPage.find('div', attrs={'class': 'content'}).find('p')  
  value = appraisalMinimumValue.text.split(':')[2].split(' ')[2]

  isAppraivsalMinimun = appraisalMinimumValue.text.split(':')[1].find("Valor mínimo de venda") != -1 

  if existValidContent(value, 0, f'id {itemPublished.id}. Appraisal Minimum Value not found.') and isAppraivsalMinimun:
    itemPublished.appraisalMinimumValue = value

def setAppraisalBetterValue(itemPublished, soupPage):
  appraisalMinimumValue = soupPage.find('div', attrs={'class': 'content'}).find('p')  
  value = appraisalMinimumValue.text.split(':')[2].split(' ')[2]

  isAppraivsalMinimun = appraisalMinimumValue.text.split(':')[1].find("Valor da melhor proposta") != -1 

  if existValidContent(value, 0, f'id {itemPublished.id}. Appraisal Minimum Value not found.') and isAppraivsalMinimun:
    itemPublished.appraisalMinimumValue = value

def setDescription(itemPublished, soupPage):
  description = soupPage.find_all('p', attrs={'style': 'margin-bottom: 0.5em;'})
  
  if existValidContent(description, 1, f'id {itemPublished.id}. Description not found.') :
    itemPublished.description = description[1].text.replace('Descrição:', '')

def setTypeProperty(itemPublished, soupPage):
  typeProperty = getValueByDescription(soupPage, 'Tipo de imóvel', 0)

  if existValidContent(typeProperty, 0, f'id {itemPublished.id}. Type of Immobile not found.') :
    itemPublished.typeProperty = typeProperty

def setNumberOfRoom(itemPublished, soupPage):
  numberOfRoom = getValueByDescription(soupPage, 'Quartos', 0)

  if existValidContent(numberOfRoom, 0, f'id {itemPublished.id}. Number of Room not found.') :
    itemPublished.numberOfRoom = numberOfRoom

def setSituation(itemPublished, soupPage):
  situation = getValueByDescription(soupPage, 'Situação', 0)

  if existValidContent(situation, 0, f'id {itemPublished.id}. Number of room not found.') :
    itemPublished.situation = situation

def setGarage(itemPublished, soupPage):
  garage = getValueByDescription(soupPage, 'Garagem', 0)

  if existValidContent(garage, 0, f'id {itemPublished.id}. Garage not found.') :
    itemPublished.garage = garage

def setTotalArea(itemPublished, soupPage):
  totalArea = getValueByDescription(soupPage, 'Área total', 1)

  if existValidContent(totalArea, 0, f'id {itemPublished.id}. Total area not found.') :
    itemPublished.totalArea = totalArea

def setPrivateArea(itemPublished, soupPage):
  privateArea = getValueByDescription(soupPage, 'Área privativa', 1)

  if existValidContent(privateArea, 0, f'id {itemPublished.id}. Private Area not found.') :
    itemPublished.privateArea = privateArea

def setLandArea(itemPublished, soupPage):
  privateArea = getValueByDescription(soupPage, 'Área do terreno', 1)

  if existValidContent(privateArea, 0, f'id {itemPublished.id}. Private Area not found.') :
    itemPublished.privateArea = privateArea
# def setAdditionalInformation(itemPublished, soupPage):

# def setTimeRemainingOnline(itemPublished, soupPage):

def getValueByDescription(soupPage, description, sidePage: int):  
  span = soupPage.find_all('div', attrs={'class': 'control-item control-span-6_12'})[sidePage].find('p').find_all('span')

  for item in span:
    if item.text.find(description) == 0:
      return item.text.replace('<',' ').replace('>',' ').split(' ')[-1]

  return None

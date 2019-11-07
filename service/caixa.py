import logging
import re
import requests
from Error import ValueNotFound, LinkNotFound
from bs4 import BeautifulSoup, Tag
import constant
from dto import ItemPublishedCaixa


def printSoup(link):
  page = requests.get(link, verify=False)
  soup = BeautifulSoup(page.text, 'html.parser')
  print(soup)

def getLinkAllImmobile(state, soup):
  allJavascript = soup.find('script', type="text/javascript").text

  link = allJavascript[allJavascript.find('"'): allJavascript.find(',')]
  link = link.replace('"', '').replace('+', '').replace(' ', '').replace('estado', state)

  return link

def initScrapingCaixa(state):
  page = requests.get(constant.URL_CAIXA, verify=False)
  soup = BeautifulSoup(page.text, 'html.parser')

  pageList = requests.get(constant.URL_CAIXA_LIST + getLinkAllImmobile('RS', soup), verify=False)

  soupList = BeautifulSoup(pageList.text, 'html.parser')

  listTr = soupList.find_all('tr')

  listOfLinks = []

  for tr in listTr:
    listTd = tr.find_all('td')
    for td in listTd:
      if td.find('a') != None and td.find('a').text.strip() == 'Detalhes':
        listOfLinks.append(td.find('a', href=True)['href'])

  return listOfLinks

def extractInformationByLink(link):
  page = requests.get(link, verify=False)
  soup = BeautifulSoup(page.text, 'html.parser')

  itemPublishedCaixa = ItemPublishedCaixa

  try:
    
    if 'erro' in soup:
      raise LinkNotFound(link)

    itemPublishedCaixa.address = findAddress(soup)
    itemPublishedCaixa.appraisalValue = findAppraisalValue(soup)
    itemPublishedCaixa.timeRemainingOnline = findTimeRemainingOnline(soup)

    #If the time remaining is not zero, the immobile is in the auction.
    #   In this case should be set the better appraisal value, else if
    #   appraisal minimun value should be set  
    if itemPublishedCaixa.timeRemainingOnline != None and itemPublishedCaixa.timeRemainingOnline != 0:
      itemPublishedCaixa.appraisalBetterValue = findAppraisalBetterValue(soup)
    else:
      itemPublishedCaixa.appraisalMinimumValue = findAppraisalMinimumValue(soup)

    itemPublishedCaixa.auctionBid = None
    itemPublishedCaixa.description = findDescription(soup)
    itemPublishedCaixa.typeImmobile = findTypeImmobile(soup)
    itemPublishedCaixa.numberOfRoom = findNumberOfRoom(soup)
    itemPublishedCaixa.situation = findSituation(soup)
    itemPublishedCaixa.totalArea = findTotalArea(soup)
    itemPublishedCaixa.privateArea = findPrivateArea(soup)
    itemPublishedCaixa.additionalInformation = findAdditionalInformation(soup)

  except ValueNotFound as err:
    logging.warning('\nError message : ' + err._msg + 
                    '\nLink: ' + link)
    #print()
    #print(printSoup(link))
    
  except LinkNotFound as err:
    logging.warning('\nError open link' + 
                    '\nLink: ' + link)

  #print(itemPublishedCaixa.__dict__)
  return itemPublishedCaixa

def existArrayIndex(arrayList, index):
  try:
    return arrayList[index] != None
  except:
    return False


def findAddress(htmlText):
  address = htmlText.find_all('p', attrs={'style': 'margin-bottom: 0.5em;'})

  if address != None and existArrayIndex(address, 0) :
    return address[0].text.replace('Endereço:', '')
  else:
    raise ValueNotFound('Address not found.')    


def findAppraisalValue(htmlText):
  appraisalValue = htmlText.find('div', attrs={'class': 'content'}).find('p')
  value = appraisalValue.text.split(':')[1].replace(' R$ ', '').replace('Valor mínimo de venda','')

  if value != None:
    return value
  else:
    raise ValueNotFound('Appraisal Value not found.') 

def findTimeRemainingOnline(htmlText):
  try:
    allJavaScript = htmlText.find('script', type="text/javascript").text
    time = allJavaScript[allJavaScript.find('strLista') + 19 : allJavaScript.find('strLista') + 38]  

    if time[0:2].isdigit():
      return time
    else:
      return None

  except:
    return None

def findAppraisalMinimumValue(htmlText):
  appraisalMinimumValue = htmlText.find('div', attrs={'class': 'content'}).find('p')
  value = appraisalMinimumValue.text.split(':')[2].replace(' R$ ', '').replace(' ( desconto de 88%)', '')
  
  if value != None:
    return value
  else:
    raise ValueNotFound('Appraisal Minimum Value not found.')

def findAppraisalBetterValue(htmlText):
  appraisalBetterValue = htmlText.find('div', attrs={'class': 'content'}).find('p')
  value = appraisalBetterValue.text.split(':')[2].replace(' R$ ', '').replace(' ( desconto de 88%)', '')
 
  if value != None and value.isdigit():
    return value
  else:
    raise ValueNotFound('Appraisal Better Value not found.')

def findDescription(htmlText):
  description = htmlText.find_all('p', attrs={'style': 'margin-bottom: 0.5em;'})
  
  if description != None and existArrayIndex(description, 1) :
    return description[1].text.replace('Descrição:', '')
  else:
    raise ValueNotFound('Description not found.')    

def findTypeImmobile(htmlText):
  typeImmobile = htmlText.find_all('div', attrs={'class': 'control-item control-span-6_12'})[0].find('p').find_all('strong')

  if existArrayIndex(typeImmobile, 0) and typeImmobile != None:
    return typeImmobile[0].text
  else:
    raise ValueNotFound('Type of Immobile not found')

def findSituation(htmlText):
  situation = htmlText.find_all('div', attrs={'class': 'control-item control-span-6_12'})[0].find('p').find_all('strong')

  if existArrayIndex(situation, 1) and situation != None:
    return situation[1].text
  else:
    raise ValueNotFound('Situation not found')

def findNumberOfRoom(htmlText):
  numberOfRoom = htmlText.find_all('div', attrs={'class': 'control-item control-span-6_12'})[0].find('p').find_all('strong')

  if existArrayIndex(numberOfRoom, 2) and numberOfRoom != None:
    return numberOfRoom[2].text
  else:
    raise ValueNotFound('Number of Room not found')

def findTotalArea(htmlText):
  totalArea = htmlText.find_all('div', attrs={'class': 'control-item control-span-6_12'})[1].find('p').find_all('span')

  for total in totalArea:
    if 'total' in total.text:
      return total.text.replace('Área total = ', '')
    
  raise ValueNotFound('Total Area not found')

def findPrivateArea(htmlText):
  privateArea = htmlText.find_all('div', attrs={'class': 'control-item control-span-6_12'})[1].find('p').find_all('span')

  for private in privateArea:
    if 'privativa' in private.text:
      return private.text.replace('Área privativa = ', '')

  raise ValueNotFound('Private Area not found')

def findAdditionalInformation(htmlText):
  additionalInformation = htmlText.find('div', attrs={'class': 'related-box'}).find_all('p')

  if additionalInformation != None and existArrayIndex(additionalInformation, 2):
    return additionalInformation[2].text.replace('\xa0', '')
  else:
    raise ValueNotFound('Additional Information not found')


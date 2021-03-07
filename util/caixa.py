import logging
import requests
import os
from typing import List

from bs4 import BeautifulSoup, Tag
from dto.link import Link
from exception.processError import ProcessError

"""
This class contains all functions that provaided the tools to scraper the 'Caixa Econômica Federal'
"""
class Caixa:
  
  def __init__(self) -> None:
    self.URL_CAIXA = os.getenv('URL_CAIXA')
    self.URL_CAIXA_LIST = os.getenv('URL_CAIXA_LIST')

  def getUrlsByState(self, state: str) -> List[Link]:
    """This function get all urls contained on the official site, based on the provided state.
    
    Arguments:
        state {str} -- Responsible for filter the list of the link by the state.
    
    Returns:
        List[Link] -- List of url getting from the website
    """ 
    logging.info(f'Getting all urls from state {state.__str__()}.')

    #returning the main page.
    mainPageRequest = requests.get(self.URL_CAIXA, verify=False)

    #converting the main page into a soup (xml).
    mainSoupPage = BeautifulSoup(mainPageRequest.text, 'html.parser')

    #returning the new page based on main page with all urls
    pageOfUrls = requests.get(self.buildMainUrl(mainSoupPage, state), verify=False)

    #converting the page whit all urls into a soup (xml).
    soupOfAllUrls = BeautifulSoup(pageOfUrls.text, 'html.parser')

    #filtering the 'tr' tag and putting it on a list.
    listOfUrlsWithTrTag = soupOfAllUrls.find_all('tr')

    if listOfUrlsWithTrTag.__len__() == 0:
      raise ProcessError(f'Fail during the getting all urls from state {state}.')

    #creating the list of links which will be returned
    links:List[Link] = []

    for trTag in listOfUrlsWithTrTag:
      
      link: Link = Link()
      
      for index in range(len(trTag.find_all('td'))):
        tdTag = trTag.find_all('td')[index]
        
        if self.isDatailTag(tdTag):
          link.url = self.getHRefPropertyLink(tdTag)

        if link.__validLink__():

          if self.isAddressTag(index):
            link.address = self.getTagTextDescritpion(tdTag)

          if self.isDistrictTag(index):
            link.district = self.getTagTextDescritpion(tdTag)

          if self.isCityTag(index):
            link.city = self.getTagTextDescritpion(tdTag)

          if self.isStateTag(index):
            link.state = self.getTagTextDescritpion(tdTag)

          links.append(link)    

    logging.info(f'It was found {links.count()} itens from state {state.__str__()}.')

    return links

  def isDatailTag(tag: Tag) -> bool:
    return tag.find('a') != None and tag.find('a').text.strip() == 'Detalhes'

  def isAddressTag(index: int) -> bool:
    return index == 1

  def isDistrictTag(index: int) -> bool:
    return index == 2

  def isCityTag(index: int) -> bool:
    return index == 9

  def isStateTag(index: int) -> bool:
    return index == 10

  def getHRefPropertyUrl(tdTag: Tag) -> str:
    return tdTag.find('a', href=True)['href']

  def getTagTextDescritpion(tdTag: Tag) -> str:
    return tdTag.text.strip()

  def buildMainUrl(self, soupPage: BeautifulSoup, state: str) -> str:
    """Based on main page, this function build the link that will list all available imovel.
    
    Arguments:
        soupPage {BeautifulSoup} -- The main page.
        state {str} -- The state of the filter.
    
    Returns:
        str -- The link with all imovel.
    """  
    logging.info(f'Building url to state {state.__str__()}.')

    javaScriptTag = soupPage.find('script', type='text/javascript').prettify()
    
    splitByQuotes = javaScriptTag.split('"')

    link = f'{splitByQuotes[3]}{state}{splitByQuotes[5]}'

    logging.info(f'Builded url: {self.URL_CAIXA_LIST}{link}')
    
    return f'{self.URL_CAIXA_LIST}{link}'
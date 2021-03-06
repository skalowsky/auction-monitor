import logging
from typing import List

from util import caixa, caixaExtractor
import util.api as api
from dto.itemPublished import ItemPublished
from enums.state import State

"""
This class contains all threads used to scraping and sand to API the 'Caixa Econômica Federal' item
"""

def scrapingCaixaJob(state: State):
  """This function is the job that get all itens by state on 'Caixa Econômica Federal' and send to API
  
  Arguments:
  
  Returns:

  """ 

  logging.info(f'Scraping from {state.__str__()} all caixa federal itens.')

  itemPublishList:List[ItemPublished] = []
  
  links = caixa.getListOfLinkByState(state.__str__())
  for link in links:
    item: ItemPublished = caixaExtractor.extractInformationsByLink(link)
    if item != None and hasattr(item, 'id'):
      itemPublishList.append(item)
  
  for item in itemPublishList:
    print(item)
  #   api.postItem(item)
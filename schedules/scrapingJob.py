from dto.link import Link
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
  # link_1:Link = Link()
  # link_2:Link = Link()
  # link_3:Link = Link()

  # link_1.url = 'https://venda-imoveis.caixa.gov.br/sistema/detalhe-imovel.asp?hdnOrigem=index&hdnimovel=1444400687014'
  # link_2.url = 'https://venda-imoveis.caixa.gov.br/sistema/detalhe-imovel.asp?hdnOrigem=index&hdnimovel=10008444'
  # link_3.url = 'https://venda-imoveis.caixa.gov.br/sistema/detalhe-imovel.asp?hdnOrigem=index&hdnimovel=1444406437648'

  # links:List[Link] = []
  # links.append(link_1)
  # links.append(link_2)
  # links.append(link_3)

  try:
    links = caixa.getListOfLinkByState(state.__str__())
  except:
    logging.error(f'Finishing process to state {state.__str__()}')
    return

  itemPublishList:List[ItemPublished] = []

  for link in links:
    try:
      item: ItemPublished = caixaExtractor.extractInformationsByLink(link)
      if item != None and hasattr(item, 'id'):
        itemPublishList.append(item)
        logging.info(f'Item successfully added {link.url}')
      else:
        logging.warning(f'No item added by the link {link.url}')
    except:
      logging.error(f'Item finished whit error. Link:{link.url}')

  for item in itemPublishList:
    print(item)
  #   api.postItem(item)

def threadGettingListOfLinkByState(state:str):
  try:
    links = caixa.getListOfLinkByState(state.__str__())
  except:
    logging.error(f'Finishing process to state {state.__str__()}')
    return
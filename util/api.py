import logging
import os
import requests

from dto.itemPublished import ItemPublished
from requests import Response
from requests.exceptions import HTTPError
from typing import List

"""
This class contains all functions that provaided the tools to call the 'scraping api'
"""
URL_AUCTION_SCRAPING_API = os.getenv('URL_AUCTION_SCRAPING_API', 'Token Not found')

def postItem(item: ItemPublished) -> bool:
  """This function calls a post request to save an item.
  
  Arguments:
      item {ItemPublished} -- Auction item which will be saved on api.
  
  Returns:
      bool -- It will return True if the api has success in persist the item.
  """ 
  logging.info(f'Sending the item {item.id} to api')
  logging.debug(f'Sending the json: {item.__json__()}')
  try:
    headers = {"Content-Type": "application/json"}
    response: Response = requests.post(url = f'{URL_AUCTION_SCRAPING_API}/auction/item', data = item.__json__(), headers = headers)
    response.raise_for_status()
  except HTTPError as http_err:
    logging.error(f'HTTP error occurred: {http_err}')
    # raise some exception
  else:
    logging.info(f'Api received the item {item.id}')

def getOpenAuction() -> List[ItemPublished]:
  """This function calls a get request to receive a list of an item which are open to a new bid.
  
  Arguments:
      item {ItemPublished} -- Auction item which will be saved on api.
  
  Returns:
      bool -- It will return True if the api has success in persist the item.
  """ 
  return None

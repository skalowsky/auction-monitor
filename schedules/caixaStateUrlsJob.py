import logging
from typing import List

from dto.itemPublished import ItemPublished
from dto.link import Link
from enums.state import State
from schedules.threadStateUrl import ThreadStateUrl
"""
This class contains all threads used to scraping and sand to API the 'Caixa Econômica Federal' item
"""
class CaixaStateUrlsJob:
  
  def __init__(self) -> None:
    self.threads:List[ThreadStateUrl] = []
    self.result:List[Link] = []

  def start(self) -> None:
    self.startThreads()
    self.appendResult()


  def startThreads(self) -> None:
    for state in State._member_names_:
      threadStateUrl:ThreadStateUrl = ThreadStateUrl(state)
      threadStateUrl.setDaemon(True)
      threadStateUrl.start()
      self.threads.append(threadStateUrl)

    for thread in self.threads:
      thread.join()

  def appendResult(self) -> None:
    for thread in self.threads:
      self.result += thread.result
    
    # try:
    #   links = caixa.getListOfLinkByState(state.__str__())
    # except:
    #   logging.error(f'Finishing process to state {state.__str__()}')
    #   return

    # itemPublishList:List[ItemPublished] = []

    # for link in links:
    #   try:
    #     item: ItemPublished = caixaExtractor.extractInformationsByLink(link)
    #     if item != None and hasattr(item, 'id'):
    #       itemPublishList.append(item)
    #       logging.info(f'Item successfully added {link.url}')
    #     else:
    #       logging.warning(f'No item added by the link {link.url}')
    #   except:
    #     logging.error(f'Item finished whit error. Link:{link.url}')

    # for item in itemPublishList:
    #   print(item)
    # #   api.postItem(item)

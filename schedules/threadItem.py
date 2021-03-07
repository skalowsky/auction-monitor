import threading
import logging
from dto.itemPublished import ItemPublished
from dto.link import Link
from util.caixaExtractor import CaixaExtractor

class ThreadItem (threading.Thread):
  
  def __init__(self, link):
    threading.Thread.__init__(self)
    self.link:Link = link
    self.result:ItemPublished

  def run(self):
    logging.error(f'Thread is starting ')

    caixaExtractor:CaixaExtractor = CaixaExtractor()
    self.result = caixaExtractor.extractInformationsByLink(self.link)
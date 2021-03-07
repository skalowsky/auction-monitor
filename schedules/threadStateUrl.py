import threading
import logging
import time
from typing import List

from dto.link import Link
from util.caixaExtractor import CaixaExtractor

class ThreadStateUrl (threading.Thread):
  
  def __init__(self, state):
    threading.Thread.__init__(self)
    self.state = state
    self.result:List[Link] = []
  
  def run(self):
    logging.error(f'Thread is starting in the state {self.state}')
    self.getUrlByState()

  def getUrlByState(self):    
    logging.info(f'thread - process of state: {self.state}')
    time.sleep(3)
    self.result.append(Link('link 1'))
    self.result.append(Link('link 2'))
    # add all itens inside of result
    logging.info(f'thread - end process of state: {self.state}')


    # caixaExtractor:CaixaExtractor = CaixaExtractor()
    # caixaExtractor.extractInformationsByLink(Link('https://venda-imoveis.caixa.gov.br/sistema/detalhe-imovel.asp?hdnOrigem=index&hdnimovel=10008444'))
    

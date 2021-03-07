import schedule
import time
import sys, getopt

import urllib3
import coloredlogs, logging

from schedules.scrapingJob import scrapingCaixaJob

from enums.state import State

def configuration():
  coloredlogs.install()
  urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # supress warning

  format: str = '%(asctime)s - %(levelname)s: %(message)s'
  datefmt: str = '%m/%d/%Y %I:%M:%S %p'
  logging.basicConfig(level=logging.INFO, format=format, datefmt=datefmt)

def jobs():
  schedule.every().day.at("12:00").do(scrapingCaixaJob, state=State.RS)

def runOnce():
  scrapingCaixaJob(State.SC)

def main():
  jobs()
  
  # while True:
  #   schedule.run_pending()
  #   time.sleep(1)

def runCustomFunctionBasedOnArgs(argv):
  try:
    opts, args = getopt.getopt(argv,"hr:",["runOnce="])
  except getopt.GetoptError:
    print ('main.py -r <true/false>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print ('test.py -r true/false')
      sys.exit()    
    if opt == '-r' and arg == 'true':
      runOnce()

# from util import caixa, caixaExtractor
# from dto.itemPublished import ItemPublished
# from dto.link import Link

if __name__ == "__main__":
  configuration()

  # runCustomFunctionBasedOnArgs(sys.argv[1:])
  runOnce()
  # main()

  # print(State._member_names_) # prints [1, 2]
  # link: Link = Link()
  # link.url = "https://venda-imoveis.caixa.gov.br/sistema/detalhe-imovel.asp?hdnOrigem=index&hdnimovel=1444400687014"

  # item: ItemPublished = caixaExtractor.extractInformationsByLink(link)
  # print('item.__json__()')
  # print(item.__json__())
  # api.postItem(item)
  # print(item)
  # caixaExtractor.extractInformationsByLink(Link(""))
  


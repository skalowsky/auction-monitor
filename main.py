from schedules.postItemJob import PostItemJob
from schedules.caixaItemJob import CaixaItemJob
import schedule
import time
import sys, getopt

import urllib3
import coloredlogs, logging

from schedules.caixaStateUrlsJob import CaixaStateUrlsJob

from enums.state import State

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

def configuration():
  coloredlogs.install()
  urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # supress warning

  format: str = '%(asctime)s - %(levelname)s: %(message)s'
  datefmt: str = '%m/%d/%Y %I:%M:%S %p'
  logging.basicConfig(level=logging.INFO, format=format, datefmt=datefmt)

# def jobs():
  # schedule.every().day.at("12:00").do(ScrapingCaixaJob().start, state=State.RS)
  # schedule.every().day.at("12:00").do(ScrapingCaixaJob().start)

def runOnce() -> None:
  # getting all urls 
  caixaStateUrlsJob:CaixaStateUrlsJob = CaixaStateUrlsJob()
  caixaStateUrlsJob.start()

  # getting all itens from urls
  caixaItemJob:CaixaItemJob = CaixaItemJob(caixaStateUrlsJob.result)
  caixaItemJob.start()

  # postting all itens
  postItemJob:PostItemJob = PostItemJob(caixaItemJob.result)
  postItemJob.start()

  print('')

def main():
  return
  # jobs()
  
  # while True:
  #   schedule.run_pending()
  #   time.sleep(1)

if __name__ == "__main__":
  configuration()

  # runCustomFunctionBasedOnArgs(sys.argv[1:])
  runOnce()
  # main()

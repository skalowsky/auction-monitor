import requests
from bs4 import BeautifulSoup, Tag
import caixa
import constant

def getLinkAllImmobile(state, soup):
  allJavascript = soup.find('script', type="text/javascript").text

  link = allJavascript[allJavascript.find('"'): allJavascript.find(',')]
  link = link.replace('"', '').replace('+', '').replace(' ', '').replace('estado', state)

  return link

def initScrapingCaixa(state):
  page = requests.get(constant.URL_CAIXA, verify=False)
  soup = BeautifulSoup(page.text, 'html.parser')

  getLinkAllImmobile(state, soup)

  pageList = requests.get(constant.URL_CAIXA_LIST + caixa.getLinkAllImmobile('RS', soup), verify=False)
  soupList = BeautifulSoup(pageList.text, 'html.parser')

  listTr = soupList.find_all('tr')

  #for listTd in listTr:

  listTd = listTr[1].find_all('td')

  print(listTd[0].find('a', href=True)['href'])
  print(listTd[0].find('a').contents[0])

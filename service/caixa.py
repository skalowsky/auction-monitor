import requests
from bs4 import BeautifulSoup, Tag
import constant
from dto import ItemPublishedCaixa

def getLinkAllImmobile(state, soup):
  allJavascript = soup.find('script', type="text/javascript").text

  link = allJavascript[allJavascript.find('"'): allJavascript.find(',')]
  link = link.replace('"', '').replace('+', '').replace(' ', '').replace('estado', state)

  return link

def initScrapingCaixa(state):
  page = requests.get(constant.URL_CAIXA, verify=False)
  soup = BeautifulSoup(page.text, 'html.parser')

  pageList = requests.get(constant.URL_CAIXA_LIST + getLinkAllImmobile('RS', soup), verify=False)

  soupList = BeautifulSoup(pageList.text, 'html.parser')

  listTr = soupList.find_all('tr')

  for tr in listTr:
    listTd = tr.find_all('td')
    for td in listTd:
      if td.find('a') != None and td.find('a').text.strip() == 'Detalhes':
        aux = td.find('a', href=True)['href']
        #print(td.find('a', href=True)['href'])

  extractInformation(aux)
  #listTd = listTr[1].find_all('td')

  #print(listTd[0].find('a', href=True)['href'])
  #print(listTd[0].find('a').contents[0])

def extractInformation(link):
  print(link)
  page = requests.get(link, verify=False)
  soup = BeautifulSoup(page.text, 'html.parser')

  findAppraisalValue(soup)

  itemPublishedCaixa: ItemPublishedCaixa = ItemPublishedCaixa
  itemPublishedCaixa.address = findAddress(soup)
  #itemPublishedCaixa.appraisalValue = findAppraisalValue(soup)

  #print(vars(itemPublishedCaixa))

  return itemPublishedCaixa
  
def findAddress(htmlText):
  address = htmlText.find('p', attrs={'style': 'margin-bottom: 0.5em;'})
  
  if address != None:
    return address.text
  else:
    print('exception')

def findAppraisalValue(htmlText):
  appraisalValue = htmlText.find('div', attrs={'class': 'content'}).find_all('h4')[0]
  #print (htmlText)
  print ( appraisalValue.text )
  #return 

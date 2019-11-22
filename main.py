from service import caixa
import urllib3
from Error import ValueNotFound
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # supress warning
logging.basicConfig(level=logging.INFO)

listOfLinks = caixa.initScrapingCaixa('RS')

#print(listOfLinks[0])
#for link in listOfLinks:
  #print(link)
print(caixa.extractInformationByLink(listOfLinks[0]))

#caixa.extractInformationByLink('https://venda-imoveis.caixa.gov.br/sistema/detalhe-imovel.asp?hdnOrigem=index&hdnimovel=1044920976112')

# Remover links inferiores
#last_links = soup.find(class_='AlphaNav')
#last_links.decompose()

# Pegar todo o texto da div BodyText
#artist_name_list = soup.find(class_='BodyText')

# Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
#artist_name_list_items = artist_name_list.find_all('a')

# Criar loop para imprimir todos os nomes de artistas
#for artist_name in artist_name_list_items:
    #names = artist_name.contents[0]
    #print(names)
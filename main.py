from util import caixa, caixaExtractor
import urllib3
import logging
import util.api as api

from dto.link import Link
from dto.itemPublished import ItemPublished

def configuration():
  urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # supress warning

  format: str = '%(asctime)s - %(levelname)s: %(message)s'
  datefmt: str = '%m/%d/%Y %I:%M:%S %p'
  logging.basicConfig(level=logging.DEBUG, format=format, datefmt=datefmt)


def main():
  links = caixa.getListOfLinkByState("RS")
  for link in links:
    print(link.__str__())
    caixaExtractor.extractInformationsByLink(link)


if __name__ == "__main__":
  configuration()
  # main()

  link: Link = Link()
  link.url = "https://venda-imoveis.caixa.gov.br/sistema/detalhe-imovel.asp?hdnOrigem=index&hdnimovel=8143700504439"
  # link.url = "https://venda-imoveis.caixa.gov.br/sistema/detalhe-imovel.asp?hdnOrigem=index&hdnimovel=1555529270042" --naõ existe mais

  item: ItemPublished = caixaExtractor.extractInformationsByLink(link)
  # print(item.__json__())
  # api.postItem(item)
  print(item)
  # caixaExtractor.extractInformationsByLink(Link(""))
  


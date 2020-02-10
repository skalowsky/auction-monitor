from util import caixa, caixaExtractor
import urllib3
import logging

from dto.link import Link

def configuration():
  urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # supress warning

  format: str = '%(asctime)s - %(levelname)s: %(message)s'
  datefmt: str = '%m/%d/%Y %I:%M:%S %p'
  logging.basicConfig(level=logging.INFO, format=format, datefmt=datefmt)



def main():
  links = caixa.getListOfLinkByState("RS")
  for link in links:
    print(link.__str__())
    caixaExtractor.extractInformationsByLink(link)


if __name__ == "__main__":
  configuration()
  main()

  # link: Link = Link()
  # link.link = "https://venda-imoveis.caixa.gov.br/sistema/detalhe-imovel.asp?hdnOrigem=index&hdnimovel=8045600010698"

  # caixaExtractor.extractInformationsByLink(link)

  #caixaExtractor.extractInformationsByLink(Link(""))
  


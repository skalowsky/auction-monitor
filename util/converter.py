from exception.scrappingError import ScrappingError

def strToFloat(value:str) -> float:
  value = value.replace('.', '').replace(',', '.')
  try:
    return float(value)
  except Exception as err:
    raise ScrappingError(err)

def strToInt(value:str) -> int:
  try:
    return int(value)
  except Exception as err:
    raise ScrappingError(err)
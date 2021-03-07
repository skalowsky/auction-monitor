from schedules.threadItem import ThreadItem
from dto.itemPublished import ItemPublished
from dto.link import Link
from typing import List


class CaixaItemJob:

  def __init__(self, listOfUrls:List[Link]) -> None:
    self.threads:List[ThreadItem] = []
    self.listOfUrls:List[Link] = listOfUrls    
    self.result:List[ItemPublished] = []

  def start(self) -> None:
    self.startThreads()
    self.appendResult()
    
  def startThreads(self) -> None:
    for url in self.listOfUrls:
      threadItem:ThreadItem = ThreadItem(url)
      threadItem.setDaemon(True)
      threadItem.start()
      self.threads.append(threadItem)

    for thread in self.threads:
      thread.join()

  def appendResult(self) -> None:
    for thread in self.threads:
      self.result.append(thread.result)
    
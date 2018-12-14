import requests
from service.exception import ServiceException

class ServiceBase:
  def get(self, url):
    if self.success():
      return self.data()
    self.raiseMessageException()

  def success(self):
    return ('success' in self.serverResponse and self.serverResponse['success'] == True)

  def data(self):
    return self.serverResponse['data']

  def message(self):
    return self.serverResponse['message'] if 'message' in self.serverResponse else ''

  def raiseMessageException(self):
    raise ServiceException(self.message())

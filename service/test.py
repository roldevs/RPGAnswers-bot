import requests
from service.base import ServiceBase
from service.exception import ServiceException

class ServiceTest(ServiceBase):
  def __init__(self, serverResponse):
    self.serverResponse = serverResponse

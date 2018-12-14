import requests
from service.base import ServiceBase

class ServiceUrl(ServiceBase):
  def __init__(self, base_url):
    self.base_url = base_url

  def get(self, url):
    r = requests.get(self.base_url + url)
    print(self.base_url + url)
    self.serverResponse = r.json()
    return super().get(url)

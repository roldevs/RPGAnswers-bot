from command.factory import CommandFactory
from service.url import ServiceUrl

def service():
  return ServiceUrl('https://hall.herokuapp.com')

def getResponse(cmd):
  try:
    return CommandFactory(service()).getCommand(cmd).execute()
  except Exception as e:
    return 'ERROR: %s' % str(e)

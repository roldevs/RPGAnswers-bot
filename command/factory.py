from command.list_locale import CommandListLocale
from command.list_system import CommandListSystem
from command.list_table import CommandListTable
from command.random_table import CommandRandomTable
from command.help import CommandHelp

class CommandFactory:
  COMMANDS = [
    CommandListLocale,
    CommandListSystem,
    CommandListTable,
    CommandRandomTable,
    CommandHelp
  ]

  def __init__(self, service):
    self.service = service

  def getCommand(self, cmd):
    for klass in self.COMMANDS:
      if klass(self.service, cmd).isCommand():
        return klass(self.service, cmd)
    raise Exception("Incorrect number of parameters or bad command.")

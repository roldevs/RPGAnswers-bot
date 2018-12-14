from command.base import CommandBase
from formatter.list import FormatterList

class CommandListLocale(CommandBase):
  def isCommand(self):
    return self.parser().isRpgList() and self.parser().optionsLength() == 0

  def header(self):
    return "These are the available languages:"

  def url(self):
    return '/api/types.json'

  def formatter(self):
    return FormatterList



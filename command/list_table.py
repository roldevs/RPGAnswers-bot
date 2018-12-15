from command.base import CommandBase
from formatter.list import FormatterList

class CommandListTable(CommandBase):
  def isCommand(self):
    return self.parser().isRpgList() and self.parser().optionsLength() == 2

  def header(self):
    return "These are the available tables for language '" + self.parser().locale() + "' and system '" + self.parser().system() + "':"

  def url(self):
    return "/api/types/%s/%s.json" % (self.parser().locale(), self.parser().system())

  def formatter(self):
    return FormatterList

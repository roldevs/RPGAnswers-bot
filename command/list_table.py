from command.base import CommandBase
from formatter.list import FormatterList

class CommandListTable(CommandBase):
  def isCommand(self):
    return self.parser().isRpgList() and self.parser().optionsLength() == 2

  def header(self):
    return "These are the available tables for language '" + self.locale() + "' and system '" + self.system() + "':"

  def url(self):
    return "/api/types/%s/%s.json" % (self.locale(), self.system())

  def formatter(self):
    return FormatterList

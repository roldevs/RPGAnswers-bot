from command.base import CommandBase
from formatter.tree import FormatterTree

class CommandRandomTable(CommandBase):
  def isCommand(self):
    return self.parser().isRpgList() and self.parser().optionsLength() == 3

  def formatter(self):
    return FormatterTree

  def header(self):
    return "Generating results:"

  def url(self):
    return "/api/random/%s/%s/%s.json" % (self.parser().locale(), self.parser().system(), self.parser().table())

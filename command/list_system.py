from command.base import CommandBase
from formatter.list import FormatterList

class CommandListSystem(CommandBase):
  def isCommand(self):
    return self.parser().isRpgList() and self.parser().optionsLength() == 1

  def header(self):
    return "These are the available systems for language '%s':" % self.locale()

  def url(self):
    return "/api/types/%s.json" % self.locale()

  def formatter(self):
    return FormatterList

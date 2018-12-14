
class CommandParse:
  def __init__(self, command):
    self.command = command

  def isRpgList(self):
    return self.command.startswith("/rpglist")

  def isHelp(self):
    return self.command.startswith("/help")

  def options(self):
    opts = self.command.split(" ")
    opts.pop(0)
    return opts

  def optionsLength(self):
    return len(self.options())


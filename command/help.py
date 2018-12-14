from command.base import CommandBase

class CommandHelp(CommandBase):
  def isCommand(self):
    return self.parser().isHelp()

  def header(self):
    return "Available commands:"

  def formatter(self):
    return Null

  def url(self):
    return ''

  def execute(self):
    return '\n'.join([
      "/rpglist [lang][system][table]: this command lists the available languages, the available systems per language, available tables inside the system and generates a random result from a table",
      "/help: lists this menu"
    ])

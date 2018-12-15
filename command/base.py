from command.parse import CommandParse

class CommandBase(object):
  def __init__(self, service, command):
    self.service = service
    self.command = command

  def isCommand(self):
    raise NotImplementedError()

  def header(self):
    raise NotImplementedError()

  def parser(self):
    return CommandParse(self.command)

  def url(self):
    raise NotImplementedError()

  def formatter(self):
    raise NotImplementedError()

  def execute(self):
    data = self.service.get(self.url())
    return '\n'.join([
      self.header(),
      self.formatter()(data).toText(),
    ])

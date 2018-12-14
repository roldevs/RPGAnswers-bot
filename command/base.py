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

  def locale(self):
    return self.parser().options()[0]

  def system(self):
    return self.parser().options()[1]

  def table(self):
    return self.parser().options()[2]

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

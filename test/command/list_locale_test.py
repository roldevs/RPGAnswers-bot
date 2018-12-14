from command.list_locale import CommandListLocale
from service.test import ServiceTest

class TestClass(object):
  def service(self):
    return ServiceTest({'success': True, 'data': ['es', 'en']})

  def instance(self, command):
    return CommandListLocale(self.service(), command)

  def isCommand(self, command):
    return self.instance(command).isCommand()

  def header(self, command):
    return self.instance(command).header()

  def url(self, command):
    return self.instance(command).url()

  def execute(self, command):
    return self.instance(command).execute()

  def test_isCommand_list(self):
    assert self.isCommand('/rpglist')

  def test_isCommand_locales(self):
    assert not self.isCommand('/rpglist es')

  def test_isCommand_systems(self):
    assert not self.isCommand('/rpglist es maze_rats')

  def test_isCommand_types(self):
    assert not self.isCommand('/rpglist es maze_rats npc')

  def test_header(self):
    assert self.header('/rpglist') == "These are the available languages:"

  def test_url(self):
    assert self.url('/rpglist') == "/api/types.json"

  def test_execute(self):
    assert self.execute('/rpglist') == '\n'.join([
      "These are the available languages:",
      "- es\n- en"
    ])

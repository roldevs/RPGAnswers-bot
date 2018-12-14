from command.list_system import CommandListSystem
from service.test import ServiceTest

class TestClass(object):
  def service(self):
    ServiceTest({})

  def service(self):
    return ServiceTest({'success': True, 'data': ['maze_rats', 'ultbox']})

  def instance(self, command):
    return CommandListSystem(self.service(), command)

  def isCommand(self, command):
    return self.instance(command).isCommand()

  def header(self, command):
    return self.instance(command).header()

  def url(self, command):
    return self.instance(command).url()

  def execute(self, command):
    return self.instance(command).execute()

  def test_isCommand_list(self):
    assert not self.isCommand('/rpglist')

  def test_isCommand_locales(self):
    assert self.isCommand('/rpglist es')

  def test_isCommand_systems(self):
    assert not self.isCommand('/rpglist es maze_rats')

  def test_isCommand_types(self):
    assert not self.isCommand('/rpglist es maze_rats npc')

  def test_header_es(self):
    assert self.header('/rpglist es') == "These are the available systems for language 'es':"

  def test_url_es(self):
    assert self.url('/rpglist es') == "/api/types/es.json"

  def test_execute(self):
    assert self.execute('/rpglist es') == '\n'.join([
      "These are the available systems for language 'es':",
      "- maze_rats\n- ultbox"
    ])

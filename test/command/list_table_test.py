from command.list_table import CommandListTable
from service.test import ServiceTest

class TestClass(object):
  def service(self):
    ServiceTest({})

  def service(self):
    return ServiceTest({'success': True, 'data': ['npc', 'animal']})

  def instance(self, command):
    return CommandListTable(self.service(), command)

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
    assert not self.isCommand('/rpglist es')

  def test_isCommand_systems(self):
    assert self.isCommand('/rpglist es maze_rats')

  def test_isCommand_types(self):
    assert not self.isCommand('/rpglist es maze_rats npc')

  def test_header_es_maze_rats(self):
    assert self.header('/rpglist es maze_rats') == "These are the available tables for language 'es' and system 'maze_rats':"

  def test_url_es_maze_rats(self):
    assert self.url('/rpglist es maze_rats') == "/api/types/es/maze_rats.json"

  def test_execute(self):
    assert self.execute('/rpglist es maze_rats') == '\n'.join([
      "These are the available tables for language 'es' and system 'maze_rats':",
      "- npc\n- animal"
    ])

from command.random_table import CommandRandomTable
from service.test import ServiceTest

class TestClass(object):
  def service(self):
    return ServiceTest({'success': True, 'data': [{'title':'Animal','children':[{'title':'Animal terrestre','text':'Elefante'}]}]})

  def instance(self, command):
    return CommandRandomTable(self.service(), command)

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
    assert not self.isCommand('/rpglist es maze_rats')

  def test_isCommand_types(self):
    assert self.isCommand('/rpglist es maze_rats npc')

  def test_header_es_maze_rats(self):
    assert self.header('/rpglist es maze_rats npc') == "Generating results:"

  def test_url_es_maze_rats(self):
    assert self.url('/rpglist es maze_rats npc') == "/api/random/es/maze_rats/npc.json"

  def test_execute(self):
    assert self.execute('/rpglist es maze_rats npc') == "Generating results:\n- [Animal]\n-- Animal terrestre: Elefante"
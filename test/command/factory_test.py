from command.list_locale import CommandListLocale
from command.list_system import CommandListSystem
from command.list_table import CommandListTable
from command.random_table import CommandRandomTable
from command.factory import CommandFactory
from service.test import ServiceTest

class TestClass(object):
  def service(self):
    ServiceTest({})

  def test_isLocaleList(self):
    assert CommandFactory(self.service()).getCommand('/rpglist').__class__ == CommandListLocale

  def test_isSystemList(self):
    assert CommandFactory(self.service()).getCommand('/rpglist es').__class__ == CommandListSystem

  def test_isTableList(self):
    assert CommandFactory(self.service()).getCommand('/rpglist es maze_rats').__class__ == CommandListTable

  def test_isRandomTable(self):
    assert CommandFactory(self.service()).getCommand('/rpglist es maze_rats npc').__class__ == CommandRandomTable

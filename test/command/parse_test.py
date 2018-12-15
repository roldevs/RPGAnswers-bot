from command.parse import CommandParse

class TestClass(object):
  def test_isRpgList(self):
    assert CommandParse('/rpglist').isRpgList()

  def test_isNoRpgList(self):
    assert not CommandParse('/help').isRpgList()

  def test_optionsLength_zero(self):
    assert CommandParse('/rpglist').optionsLength() == 0
    assert CommandParse('/rpglist').locale() == None
    assert CommandParse('/rpglist').system() == None
    assert CommandParse('/rpglist').table() == None

  def test_optionsLength_one(self):
    assert CommandParse('/rpglist es').optionsLength() == 1
    assert CommandParse('/rpglist es').locale() == 'es'
    assert CommandParse('/rpglist es').system() == None
    assert CommandParse('/rpglist es').table() == None

  def test_optionsLength_two(self):
    assert CommandParse('/rpglist es maze_rats').optionsLength() == 2
    assert CommandParse('/rpglist es maze_rats').locale() == 'es'
    assert CommandParse('/rpglist es maze_rats').system() == 'maze_rats'
    assert CommandParse('/rpglist es maze_rats').table() == None

  def test_optionsLength_three(self):
    assert CommandParse('/rpglist es maze_rats npc').optionsLength() == 3
    assert CommandParse('/rpglist es maze_rats npc').locale() == 'es'
    assert CommandParse('/rpglist es maze_rats npc').system() == 'maze_rats'
    assert CommandParse('/rpglist es maze_rats npc').table() == 'npc'

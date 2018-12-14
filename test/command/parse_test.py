from command.parse import CommandParse

class TestClass(object):
  def test_isRpgList(self):
    assert CommandParse('/rpglist').isRpgList()

  def test_isNoRpgList(self):
    assert not CommandParse('/help').isRpgList()

  def test_optionsLength_zero(self):
    assert CommandParse('/rpglist').optionsLength() == 0

  def test_optionsLength_one(self):
    assert CommandParse('/rpglist es').optionsLength() == 1

  def test_optionsLength_two(self):
    assert CommandParse('/rpglist es maze_rats').optionsLength() == 2

  def test_optionsLength_three(self):
    assert CommandParse('/rpglist es maze_rats npc').optionsLength() == 3

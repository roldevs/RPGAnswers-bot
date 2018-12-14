from formatter.tree import FormatterTree

class TestClass(object):
  def data(self):
    return [{'title':'Animal','children':[{'title':'Animal terrestre','text':'Elefante'}]}]

  def expectedList(self):
    return [
      [1, '[Animal]'],
      [2, 'Animal terrestre: Elefante'],
    ]

  def expectedText(self):
    return '- [Animal]\n-- Animal terrestre: Elefante'

  def test_formatterList(self):
    assert FormatterTree(self.data()).toList() == self.expectedList()

  def test_formatterText(self):
    assert FormatterTree(self.data()).toText() == self.expectedText()

from formatter.list import FormatterList

class TestClass(object):
  def locales(self):
    return ['es', 'en']

  def toFormatInfo(self, text):
    return [1, text]

  def expectedList(self):
    return list(map(self.toFormatInfo, self.locales()))

  def expectedText(self):
    return "- es\n- en"

  def test_formatterList(self):
    assert FormatterList(self.locales()).toList() == self.expectedList()

  def test_formatterText(self):
    assert FormatterList(self.locales()).toText() == self.expectedText()

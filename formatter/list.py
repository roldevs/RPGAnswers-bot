from formatter.base import FormatterBase

class FormatterList(FormatterBase):
  def processData(self):
    for line in self.data:
      self.appendToLines(1, line)

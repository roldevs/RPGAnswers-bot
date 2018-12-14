
class FormatterBase(object):
  def __init__(self, data):
    self.data = data
    self.lines = []

  def processData(self):
    raise NotImplementedError()

  def toList(self):
    self.processData()
    return self.lines

  def appendToLines(self, indent, text):
    self.lines.append([indent, text])

  def indentString(self, level):
    return level * '-'

  def lineToText(self, line):
    return '%s %s' % (self.indentString(line[0]), self.sanitizeText(line[1]))

  def toText(self):
    self.processData()
    return '\n'.join(map(self.lineToText, self.lines))

  def sanitizeText(self, text):
    return text.replace(".yml", "")


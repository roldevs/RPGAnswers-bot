from formatter.base import FormatterBase

class FormatterTree(FormatterBase):
  def processData(self):
    for line in self.data:
      self.processLine(line, 1)

  def processLine(self, node, indent):
    if 'children' in node:
      self.appendToLines(indent, "[%s]" % node['title'])
      for child in node['children']:
        self.processLine(child, indent + 1)
      return
    self.appendToLines(indent, "%s: %s" % (node['title'], node['text']))

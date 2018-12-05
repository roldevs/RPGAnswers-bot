from botline import *

class botresponse:
    header = ""
    lines = []

    def __init__(self):
        self.header = ""
        self.lines = []

    def setHeader(self, newHeader):
        if isinstance(newHeader, str):
            self.header = newHeader
        else:
            raise ValueError("Header is trying to be set without a string type")

    def addLine(self, line):
        if isinstance(line, botline):
            self.lines.append(line)
        else:
            raise ValueError("A line is trying to be added without botline type")

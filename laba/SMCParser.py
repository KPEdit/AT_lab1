import base
from utils import laba1_sm

class SMCParser(base.IParser):

  __NUMS = '1234567890'
  __STRS = 'qwertyuiopasdfghjklzxcvbnm'
  __TYPES = {'int', 'short', 'long'}
  _batch = ''
  _saved = []
  _c: str
  
  def __init__(self):
    super().__init__()
    self._fsm = laba1_sm.Laba_sm(self)

  def clear(self):
    super().clear()
    self._fsm.setState(laba1_sm.LabaMap.Start)
    self._batch = ''

  @staticmethod
  def normStr(s: str):
    return ' '.join(s.split()).lower()

  def parse(self, inp: str, *args, **kwargs):
    self.clear()
    prev = []
    for self._c in self.normStr(inp):
      prev.append(type(self._fsm.getState()))
      if self._c in self.__STRS:
        self._fsm.char()
      elif self._c in self.__NUMS:
        self._fsm.num()
      elif self._c == ' ':
        self._fsm.space()
      elif self._c == '=':
        self._fsm.asg()
      else:
        self._fsm.end()
    self._fsm.end()
    if type(self._fsm.getState()) is laba1_sm.LabaMap_OK:
      if len(self._saved) == 2:
        self._node_val.type = self._saved.pop(0)
      self._node_val.val = self._saved.pop()
      return self._node_val
    return self._node_val.clear()

  def restoreBatch(self):
    self._batch = ''

  def nameGuard(self):
    return len(self._batch) <= 16

  def typeGuard(self):
    return self._batch in self.__TYPES

  def nullGuard(self):
    return len(self._batch) == 0

  def addC(self):
    self._batch += self._c

  def saveName(self):
    if self._batch != '':
      self._saved.append(self._batch)
    self.restoreBatch()

  def saveLine(self):
    self._node_val.line = self._batch
    self.restoreBatch()

  def saveType(self):
    self._saved.append(self._batch)
    self.restoreBatch()

if __name__ == '__main__':
  m = SMCParser()
  test = '768 as = short'
  print(m.parse(test))
  
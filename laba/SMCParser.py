import base
from utils import laba1_sm

class SMCParser(base.IParser):

  __TYPES = {'int', 'short', 'long'}
  __NUMS = '1234567890'
  __STRS = 'qwertyuiopasdfghjklzxcvbnm'
  
  def __init__(self):
    super().__init__()
    self._fsm = laba1_sm.Laba_sm(self)

  def clear(self):
    super().clear()
    self._fsm.setState(laba1_sm.LabaMap.Start)

  def parse(self, inp: str, *args, **kwargs):
    self.clear()
    tokens = inp.split()
    for token in tokens:
      if self.checkType(token):
        self._fsm.type()
      elif self.checkNum(token):
        self._fsm.num(token)
      elif self.checkName(token):
        self._fsm.name(token)
      elif self.checkAsign(token):
        self._fsm.asg()
      else:
        self._fsm.end()
    self._fsm.end()
    if type(self._fsm.getState()) is laba1_sm.LabaMap_OK:
      return self._node_val
    return "Incorrect"

  def setLine(self, line):
    self._node_val.line = line

  def setName(self, name):
    self._node_val.val = name

  def checkType(self, token):
    return token in self.__TYPES

  def checkNum(self, token):
    if token[0] == '0':
      if len(token) == 1:
        return True
      else:
        return False
    for c in token:
      if not ('0' <= c <= '9'):
        return False
    return True

  def checkName(self, token: str):
    if len(token) > 16:
      return False
    token = token.lower()
    if not token[0] in self.__STRS:
      return False
    for c in token[1:]:
      if not (c in self.__NUMS or c in self.__STRS):
        return False
    return True

  def checkAsign(self, token):
    return token == '='
  
  def go_to_Default(self):
    pass

import base
import ply.lex as lex
from ply.lex import Lexer, Token

class LexParser(base.IParser):
  tokens = (
    'TYPE',
    'NUMBER',
    'ASSIGN',
    'NAME',
  )

  tokens_list = []

  t_ASSIGN = r'='

  def t_TYPE(self, t):
    r'int|short|long'
    return t

  def t_NUMBER(self,t):
    r'\d+'
    if str(int(t.value)) == t.value:
      t.value = int(t.value)
      return t

  def t_NAME(self, t):
    r'[a-zA-Z][a-zA-Z0-9]{,15}'
    t.value = t.value.lower()
    return t

  t_ignore  = ' \t'

  def t_error(self,t):
    t.lexer.skip(1)

  def build(self,**kwargs):
    self.lexer:Lexer = lex.lex(module=self, **kwargs)
    return self

  def genTokens(self, inp):
    self.lexer.input(inp)
    while True:
      tok = self.lexer.token()
      if not tok:
        break
      self.tokens_list.append(tok)
    return self.tokens_list
    
  def check(self):
    if len(self.tokens_list) < 2:
      return False
    token = self.tokens_list.pop(0)
    if token.type != 'NUMBER':
      return False
    self.setLine(token.value)

    token = self.tokens_list.pop(0)
    if token.type == 'NAME':
      self.setVal(token.value)
    elif token.type == 'TYPE' and len(self.tokens_list) > 0:
      token = self.tokens_list.pop(0)
      if token.type == 'NAME':
        self.setVal(token.value)
      else:
        return False
    else:
      return False
    
    if not len(self.tokens_list):
      return True
    token = self.tokens_list.pop(0)
    if token.type != 'ASSIGN' or not len(self.tokens_list):
      return False
    token = self.tokens_list.pop(0)
    if not (token.type == 'NUMBER' or token.type == 'NAME') or len(self.tokens_list):
      return False
    return True

  def parse(self, inp: str, *args, **kwargs):
    self.clear()
    self.genTokens(inp)
    res = self.check()
    if res:
      return self._node_val
    return 'Incorrect'

  def clear(self):
    super().clear()
    self.tokens_list = []
    
  def setLine(self, line):
    self._node_val.line = line

  def setVal(self, val):
    self._node_val.val = val
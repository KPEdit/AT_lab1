import base
import ply.lex as lex
from ply.yacc import yacc, LRParser
from ply.lex import Lexer, TOKEN

_TYPES = {'int', 'short', 'long'}
_NUM = r'[1-9]\d*|0'
_NAME = r'[a-zA-Z][a-zA-Z\d]{,15}'

class LexParser(base.IParser):
  tokens = (
    'TYPE',
    'NUM',
    'NAME',
    'VARNAME',
    'VARNUM'
  )

  states = (
    ('var',   'exclusive'),
  )

  reserved = {
    'int' : 'TYPE',
    'short' : 'TYPE',
    'long' : 'TYPE',
  }

  tokens_list = []

  t_ignore = ''

  @TOKEN(_NUM)
  def t_NUM(self, t):
    return t

  def t_TYPE(self, t):
    r'[ \t]+(int|short|long)[ \t]+'
    return t

  @TOKEN(_NAME)
  def t_NAME(self, t):
    return t

  def t_var(self, t):
    r'[ \t]*=[ \t]*'
    cs = t.lexer.current_state()
    if cs == 'INITIAL':
      t.lexer.begin('var')
    else:
      t.lexer.begin('INITIAL')

  @TOKEN(_NUM+r"$")
  def t_var_VARNUM(self, t):
    t.lexer.begin('INITIAL')
    return t

  @TOKEN(_NAME+r"$")
  def t_var_VARNAME(self, t):
    t.lexer.begin('INITIAL')
    t.type = self.reserved.get(t.value, 'VARNAME')
    return t

  def t_var_error(self, t):
    t.lexer.skip(1)
    return False

  def t_error(self,t):
    t.lexer.skip(1)
    return False

  def build(self,**kwargs):
    self.lexer:Lexer = lex.lex(module=self, **kwargs)
    self.yacparser:LRParser = yacc(module=self)
    return self

  def genTokens(self, inp):
    self.lexer.input(inp)
    while True:
      try:
        tok = self.lexer.token()
      except lex.LexError as e:
        print(e)
        self.clear()
        return False
      if not tok:
        break
      self.tokens_list.append(tok)
    return self.tokens_list

  def p_num(self, p):
    """num  : NUM TYPE NAME VARNAME 
            |  NUM TYPE NAME
            | NUM TYPE NAME VARNUM"""
    self._node_val.line = p[1]
    self._node_val.val = p[3]

  def p_num2(self, p):
    """num  : NUM NAME VARNAME 
            |  NUM NAME
            | NUM NAME VARNUM"""
    self._node_val.line = p[1]
    self._node_val.val = p[2]

  def p_error(self, p):
    return None

  def parse(self, inp: str, *args, **kwargs):
    self.clear()
    self.yacparser.parse(inp)
    return self._node_val

  def clear(self):
    super().clear()
    self.tokens_list = []
    
  def setLine(self, line):
    self._node_val.line = line

  def setVal(self, val):
    self._node_val.val = val

if __name__ == '__main__':
  m = LexParser().build()
  test = '123 int inthaAH = asdh'
  test2 = '123 int asdf='
  
  print(m.parse(test))
  print(m.parse(test2))
  
import base
import ply.lex as lex
from ply.lex import Lexer

_TYPES = {'int', 'short', 'long'}

class LexParser(base.IParser):
  tokens = (
    'NUM',
    'TYPE',
    'NAME',
    'SPACE',
    # 'END',
    'ASSIGN'
  )

  tokens_list = []

  t_NUM = r"\d+"
  t_NAME = r"[a-zA-Z][a-zA-Z\d]{,15}"
  t_SPACE = r"[ \t]+"
  
  t_ignore = r""

  def t_TYPE(self, t):
    r"(int|short|long)[ \t]+"
    t.value = t.value.split()[0]
    return t

  def t_error(self,t):
    return False

  def t_ASSIGN(self, t):
    r'[ \t]*=[ \t]*'
    return t

  # def t_END(self, t):
  #   r"[\w\W]*$"
  #   self.lexer.begin('INITIAL')

  def build(self,**kwargs):
    self.lexer:Lexer = lex.lex(module=self, **kwargs)
    return self

  def genTokens(self, inp):
    self.lexer.input(inp)
    while True:
      try:
        tok = self.lexer.token()
      except lex.LexError:
        self.clear()
        return False
      if not tok:
        break
      self.tokens_list.append(tok)
    return self.tokens_list
    
  def check(self):
    '''It should be try...except'''
    if not (3 <= len(self.tokens_list) < 7):
      return False
    line = self.tokens_list.pop(0)
    if line.type != 'NUM':
      return False
    self._node_val.line = line.value
    tmp = self.tokens_list.pop(0)
    if tmp.type != 'SPACE':
      self.clear()
      return False
    tmp = self.tokens_list.pop(0)
    if tmp.type == 'TYPE':
      if len(self.tokens_list) <= 0:
        self.clear()
        return False
      if len(self.tokens_list) == 2 \
          and self.tokens_list[0].type == 'ASSIGN'\
          and (self.tokens_list[1].type == 'NAME' or self.tokens_list[1].type == 'NUM'):
        self._node_val.val = tmp.value
        return True
      else:
        self._node_val.type = tmp.value
      tmp = self.tokens_list.pop(0)
    if tmp.type != 'NAME':
      self.clear()
      return False
    self._node_val.val = tmp.value
    if len(self.tokens_list) == 0:
      return True
    if len(self.tokens_list) != 2:
      self.clear()
      return False
    tmp = self.tokens_list.pop(0)
    if tmp.type != 'ASSIGN':
      self.clear()
      return False
    tmp = self.tokens_list.pop(0)
    if tmp.type != 'NAME' and tmp.type != 'NUM':
      self.clear()
      return False
    return True 

  def parse(self, inp: str, *args, **kwargs):
    self.clear()
    self.genTokens(inp.lower().strip())
    res = self.check()
    if res:
      return self._node_val
    return base.NodeVal()

  def clear(self):
    super().clear()
    self.tokens_list = []
    

if __name__ == '__main__':
  m = LexParser().build()
  test = '768 int = asd'
  print(m.parse(test))
  test = "123 int asdf  =   asd "
  print(m.parse(test))
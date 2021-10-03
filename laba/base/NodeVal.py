
class NodeVal(object):

  line: int
  _val: int or str

  @property
  def val(self):
    return self._val

  @val.setter
  def val(self, var: int or str):
    if type(var) == type(''):
      self._val = var.lower()
    else:
      self._val = var

  def __init__(self, line=None, var=None) -> None:
    self.line = line
    self.val = var

  def clear(self):
    self.line = None
    self.val = None

  def __str__(self) -> str:
    return f"({self.line} - {self.val})"
  
  def __repr__(self) -> str:
    return f"({self.line} - {self.val})"
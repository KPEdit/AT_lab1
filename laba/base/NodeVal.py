
class NodeVal(object):

  line: int or str
  _val: int or str
  _type: str

  @property
  def val(self):
    return self._val

  @val.setter
  def val(self, var: int or str):
    if type(var) == type(''):
      self._val = var.lower()
    else:
      self._val = var

  @property
  def type(self):
    return self._type
  
  @type.setter
  def type(self, t: str or None):
    if t is None:
      self._type = 'int'    # строки может и не быть, но тип есть всегда))
    else:
      self._type = t

  def __init__(self, line=None, var=None, type_=None) -> None:
    self.line = line
    self.val = var
    self.type = type_

  def clear(self):
    self.line = None
    self.val = None
    self.type = None
    return self

  def __bool__(self):
    return not (self.line == None or self.val == None)

  def __str__(self) -> str:
    if self:
      return f"({self.line} - {self.val})"
    return "Incorrect"
  
  def __repr__(self) -> str:
    if self:
      return f"({self.line} - {self.val})"
    return "Incorrect"

  def copy(self):
    return NodeVal(self.line, self.val, self.type)
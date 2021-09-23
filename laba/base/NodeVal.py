
class NodeVal(object):

  line: int
  val: int or str

  def __init__(self, line=None, val=None) -> None:
    self.line = line
    self.val = val

  def clear(self):
    self.line = None
    self.val = None

  def __str__(self) -> str:
    return f"({self.line} - {self.val})"
  
  def __repr__(self) -> str:
    return f"({self.line} - {self.val})"
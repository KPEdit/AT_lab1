import base
import typing

class Statistics:
  parser: base.IParser
  variables: typing.Dict[str, base.NodeVal]

  def __init__(self, parser: base.IParser=None) -> None:
    self.parser = parser
    self.variables = dict()

  def clear(self):
    self.variables = dict()
  
  def parse(self, inp: str) -> base.NodeVal:
    res = self.parser.parse(inp)
    if res:
      if res.val in self.variables:
        if res.type != self.variables[res.val].type:
          return res
      else:
        self.variables[res.val] = res.copy()
    return res.clear()

  def __call__(self, inp: str, *args, **kwargs) -> base.NodeVal:
    return self.parse(inp)
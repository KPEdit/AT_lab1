import re
import base

_PATTERN = r"^(?P<line>[1-9]\d*)\s((?P<type>int|short|long)\s)?(?P<name>[a-zA-Z][\da-zA-Z]{,15})(\s=\s(?P<value>[a-zA-Z][\da-zA-Z]{,15}|\d+))?$"


class RegexParser(base.IParser):
  pattern: str
  
  def __init__(self):
    super().__init__()
    self.pattern = re.compile(_PATTERN)

  def parse(self, inp: str, *args, **kwargs):
    res = self.pattern.match(inp)
    if res is None:
      return "Incorrect"
    end = base.NodeVal(int(res.group('line')), res.group('name'))
    return end
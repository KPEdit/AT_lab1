import re
import base

# _PATTERN = r"^(?P<line>[1-9]\d*|0)[ \t]+((?P<type>int|short|long)[ \t]+)?(?P<name>[a-zA-Z][\da-zA-Z]{,15})[ \t]*(=[ \t]+(?P<value>[a-zA-Z][\da-zA-Z]{,15}|[1-9]\d*|0))?$"

# _PATTERN = r"^(?P<line>[1-9]\d*|0)[ \t]+(((?P<type>int|short|long)[ \t]+)?(?!(short|int|long)[ \t]*$))(?P<name>[a-zA-Z][\da-zA-Z]{,15})[ \t]*(=[ \t]+(?P<value>[a-zA-Z][\da-zA-Z]{,15}|[1-9]\d*|0))?$"

_PATTERN = r"^(?P<line>[1-9]\d*|0)[ \t]+(((?P<type>int|short|long)[ \t]+)?(?!(short|int|long)[ \t]*$))(?P<name>[a-zA-Z][\da-zA-Z]{,15})[ \t]*(=[ \t]+(?!(int|short|long)[ \t]*$)(?P<value>[a-zA-Z][\da-zA-Z]{,15}|[1-9]\d*|0))?$"

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
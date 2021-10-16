import re
import base

_PATTERN = r"(?P<line>\d+)[ \t]+((?P<type>int|short|long)[ \t]+)?(?P<name>[a-zA-Z][a-zA-Z\d]{,15})([ \t]*=[ \t]*([a-zA-Z][a-zA-Z\d]{,15}|\d+))?[ \t]*$"

class RegexParser(base.IParser):
  pattern: str
  
  def __init__(self):
    super().__init__()
    self.pattern = re.compile(_PATTERN)

  def parse(self, inp: str, *args, **kwargs):
    res = self.pattern.match(inp)
    if res is None:
      return base.NodeVal()
    end = base.NodeVal(res.group('line'), res.group('name').lower(), type_=res.group('type'))
    return end

if __name__ == '__main__':
  m = RegexParser()
  test = '4232760391926351 \t\t\t\tshort \t  ai  = kw'
  print(m.parse(test))
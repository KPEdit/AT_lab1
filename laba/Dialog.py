import sys
import base
from RegexParser import RegexParser
from SMCParser import SMCParser
from LexParser import LexParser

class IODialog(object):
  
  _DEFAULT_LOG = 'log.log'

  def __init__(self, parser: base.IParser):
    retcode = 0
    if len(sys.argv) == 1:
      print("Press (linux) Ctrl+D or (Windows) Ctrl+Z to exit")
      print("Enter strings to check")
      try:
        while True:
          s = input()
          print(f"Result: {parser.parse(s)}")
      except EOFError:
        print("Good bye!")
    elif len(sys.argv) <= 3:
      logFile = sys.argv[2] if len(sys.argv) == 3 else self.DEFAULT_LOG
      inpFile = sys.argv[1]
      with open(logFile, 'w+', encoding='UTF-8') as log:
        with open(inpFile, 'r', encoding='UTF-8') as inp:
          for line in inp.readlines():
            res = parser.parse(line)
            log.write(str(res)+'\n')
    else:
      print("Too much arguments were passed")
      retcode = 1
    sys.exit(retcode)

if __name__ == '__main__':
  print("1. SMC\n2. LeX\n Other. regex")
  print("Select parser: ")
  res = input()
  if res == '1':
    IODialog(SMCParser())
  elif res == '2':
    parser = LexParser()
    parser.build()
    IODialog(parser)
  else:
    IODialog(RegexParser())

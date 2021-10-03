import sys, os
from Dialog import IODialog

from RegexParser import RegexParser
from SMCParser import SMCParser
from LexParser import LexParser

if __name__ == '__main__':
  if len(sys.argv) < 3:
    raise ArithmeticError()

  smc = SMCParser()
  lex = LexParser()
  lex.build()
  regex = RegexParser()

  parsers = [
    ('SMC', smc),
    ('LeX', lex),
    ('Regex', regex),
  ]

  # print(sys.argv[1])
  with open(sys.argv[1], 'r', encoding='UTF-8') as inp:
    for p in parsers:
      fileName = p[0]+'_' \
        +os.path.basename(sys.argv[1]).split('.')[0]+'.log'
      filePath = os.path.join(sys.argv[2], fileName)
      print(filePath)
      with open(filePath, 'w+', encoding='UTF-8') as out:
        line = inp.readline()
        while line:
          res = str(p[1].parse(line.lower())) + '\n'
          out.write(res)
          line = inp.readline()
        inp.seek(0)
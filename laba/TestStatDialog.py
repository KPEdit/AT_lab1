import sys, os
from Dialog import IODialog
from Statistics import Statistics
from RegexParser import RegexParser
from SMCParser import SMCParser
from LexParser import LexParser

if __name__ == '__main__':
  if len(sys.argv) < 3:
    raise ArithmeticError()

  smc = SMCParser()
  lex = LexParser().build()
  regex = RegexParser()

  parsers = [
    ('SMC', Statistics(smc)),
    ('LeX', Statistics(lex)),
    ('Regex', Statistics(regex)),
  ]

  # print(sys.argv[1])
  with open(sys.argv[1], 'r', encoding='UTF-8') as inp:
    for p in parsers:
      fileName = 'stat_'+p[0]+'_' \
        +os.path.basename(sys.argv[1]).split('.')[0]+'.log'
      filePath = os.path.join(sys.argv[2], fileName)
      print(filePath)
      with open(filePath, 'w+', encoding='UTF-8') as out:
        line = inp.readline()
        while line:
          res = p[1].parse(line)
          if res:
            out.write(str(res)+'\n')
          line = inp.readline()
        inp.seek(0)
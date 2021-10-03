import sys, os, random, datetime
import rstr


_TEST_ENDING = '.test'
_LINE = r"([1-9]\d{,16})[ \t]{1,5}"
_TYPE = ['int', 'short', 'long']
_NAME = r"([a-zA-Z][\da-zA-Z]{,15})[ \t]{1,5}"
_VALUE = f"=[ \t]{1,5}({_NAME}|\d{1,16})" 
_NOISE = r"[^\n\v\f\r]{2,30}"
_NOISE_2 = r"[^\n\v\f\r]"
_CPATTERN = r"^(?P<line>[1-9]\d{,16})[ \t]{1,5}((?P<type>int|short|long)[ \t]{1,5})?(?P<name>[a-zA-Z][\da-zA-Z]{,15})([ \t]{1,5}=[ \t]{1,5}(?P<value>[a-zA-Z][\da-zA-Z]{,15}|\d{,16}))?$"

_RCW = .6
_RFIW = .2
_RIP = .5

def genStr(maxLen):
  if random.random() <= _RCW:
    return rstr.xeger(_CPATTERN)
  elif random.random() <= _RFIW:
    tmp = "(" + _NOISE_2 + "{" + str(maxLen//2) + ',' + str(maxLen) + '})'
    return rstr.xeger(tmp)
  else:
    tmp = ""
    if random.random() <= _RIP:
      tmp += _LINE
      if random.random() <= _RIP:
        tmp += _TYPE[random.randint(0, len(_TYPE)-1)]
      if random.random() <= _RIP:
        tmp += _NAME
        if random.random() <= _RIP:
          tmp += _VALUE
          tmp += _NOISE
    mn = max(maxLen - len(tmp), 0)
    tmp += "(" + _NOISE_2 + "{" + str(mn//2) + ',' + str(mn) + '})'
    return rstr.xeger(tmp)

def generate(testDir: str="./", N: int=10, maxLen: int=30):
  tmp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + f"__{N}__{maxLen}{_TEST_ENDING}"
  path = os.path.join(testDir, tmp)
  with open(path, 'w+', encoding='UTF-8') as out:
    for i in range(N):
      out.write(genStr(maxLen)+'\n')
  return path

if __name__ == '__main__':
  if len(sys.argv) != 4:
    print("Incorrect argv number")
    sys.exit(1) 
  else:
    path = generate(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    print(f"Done. Saved at {path}")
  # for i in range(100):
  #   print(genStr(250))
  #   print(rstr.xeger(_CPATTERN))


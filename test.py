import time

def timing(a: str, iters=1e7):
  start = time.time_ns()
  for i in range(int(iters)):
    b = a.replace('\n', '')
  end = time.time_ns()
  delta = end - start
  print(f"delta: {delta}")

  start = time.time_ns()
  for i in range(int(iters)):
    b = a[:-1] if a[-1] == '\n' else a
  end = time.time_ns()
  delta2 = end-start

  start = time.time_ns()
  for i in range(int(iters)):
    b = a.split('\n')[0]
  end = time.time_ns()
  delta3 = end-start
  print(f"delta2: {delta2}")
  print(f"delta3: {delta3}")
  print(f"delta - delta2: {delta-delta2}")
  print(a.replace('\n', ''))
  print(a[:-1] if a[-1] == '\n' else a)
  print(a.split('\n')[0])

if __name__ == '__main__':
  timing("asdgaskjdfasdf\n")
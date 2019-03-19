# importing the required modules
import timeit
import os


def benchIt(dir):
  if not dir:
    raise ValueError("Parameter 'dir' is required.")

  SETUP_CODE = '''
from {dir} import json_loads
  '''.format(**locals())

  TEST_CODE = '''
x = json_loads.loadIt()'''.format(**globals())

  # timeit.repeat statement
  times = timeit.repeat(
    setup=SETUP_CODE,
    stmt=TEST_CODE,
    repeat=5,
    number=5000
    )

  # printing minimum exec. time
  return min(times)


if __name__ == "__main__":
  print("\nRunning benchmark 'json_loads'.".format(**globals()))
  print("---------------------------------")

  dictTimes = dict()

  for benchName in ['Python', 'Nuitka', 'Numba', 'Nim']:
    dirName = '_'+benchName
    path    = os.getcwd()+os.path.sep+dirName
    if os.path.exists(os.path.abspath(path)):
      time = benchIt(dirName)
      dictTimes[benchName] = time
      speedup = dictTimes['Python'] / time
      print('{benchName:7}: {time:.4f}s'.format(**locals()) + '{speedup:>40,.2f}x'.format(**locals()))

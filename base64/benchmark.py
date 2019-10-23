# importing the required modules
import timeit
import os

TEXT = "The quick brown fox jumped over the lazy dog."


def benchIt(dir):
  if not dir:
    raise ValueError("Parameter 'dir' is required.")

  if dir == "_V":
    SETUP_CODE = '''
from ctypes import CDLL
lib = CDLL("./{dir}/b64.so")
  '''.format(**locals())

    TEST_CODE = '''
x = lib.b64__b64e("{TEXT}")
assert lib.b64__b64d(x) == "{TEXT}"'''.format(**globals())  
  else:
    SETUP_CODE = '''
from {dir} import b64
  '''.format(**locals())

    TEST_CODE = '''
x = b64.b64e("{TEXT}")
assert b64.b64d(x) == "{TEXT}"'''.format(**globals())

  # timeit.repeat statement
  times = timeit.repeat(
    setup=SETUP_CODE,
    stmt=TEST_CODE,
    repeat=10,
    number=100000
    )

  # printing minimum exec. time
  return min(times)


if __name__ == "__main__":
  print("\nRunning benchmark 'base64'".format(**globals()))
  print("---------------------------------------------------------")

  dictTimes = dict()

  for benchName in ['Python', 'Nuitka', 'Cython', 'Numba', 'Nim', 'V']:
    dirName = '_'+benchName
    path    = os.getcwd()+os.path.sep+dirName
    if os.path.exists(os.path.abspath(path)):
      time = benchIt(dirName)
      dictTimes[benchName] = time
      speedup = dictTimes['Python'] / time
      print('{benchName:7}: {time:.4f}s'.format(**locals()) + '{speedup:>40,.2f}x'.format(**locals()))

# importing the required modules
import timeit
import os

working_dir = os.path.dirname(os.path.abspath(__file__))

PLACES = 30


def python_fib_rec():
  SETUP_CODE = '''
from Python import fib_rec
  '''

  TEST_CODE = '''
x = fib_rec.fibRec({PLACES})'''.format(**globals())

  # timeit.repeat statement
  times = timeit.repeat(
    setup=SETUP_CODE,
    stmt=TEST_CODE,
    repeat=3,
    number=20
    )

  # printing minimum exec. time
  return min(times)


def nuitka_fib_rec():
  SETUP_CODE = '''
from Nuitka import fib_rec
'''

  TEST_CODE = '''
x = fib_rec.fibRec({PLACES})'''.format(**globals())

  # timeit.repeat statement
  times = timeit.repeat(
    setup=SETUP_CODE,
    stmt=TEST_CODE,
    repeat=3,
    number=20
    )

  # printing minimum exec. time
  return min(times)


def nim_fib_rec():
  SETUP_CODE = '''
from Nim import fib_rec
  '''

  TEST_CODE = '''
x = fib_rec.fibRec({PLACES})'''.format(**globals())

  # timeit.repeat statement
  times = timeit.repeat(
    setup=SETUP_CODE,
    stmt=TEST_CODE,
    repeat=3,
    number=20
    )

  # printing minimum exec. time
  return min(times)


def cython_fib_rec():
  SETUP_CODE = '''
from _Cython import fib_rec
  '''.format(**globals())

  TEST_CODE = '''
x = fib_rec.fibRec({PLACES})'''.format(**globals())

  # timeit.repeat statement
  times = timeit.repeat(
    setup=SETUP_CODE,
    stmt=TEST_CODE,
    repeat=3,
    number=20
    )

  # printing minimum exec. time
  return min(times)


if __name__ == "__main__":
  print("\nRunning benchmark 'fibonacci_recursive' to {PLACES} places.".format(**globals()))
  print("---------------------------------------------------"+('-'*len(str(PLACES))))

  min_time_python = python_fib_rec()
  print('Pure Python : {min_time_python:.4f}s'.format(**locals()))
  
  min_time_nuitka = nuitka_fib_rec()
  diff_nuitka = min_time_python / min_time_nuitka
  print('Nuitka      : {min_time_nuitka:.4f}s'.format(**locals()) + '{diff_nuitka:>40,.2f}x'.format(**locals()))
  
  min_time_cython = cython_fib_rec()
  diff_cython = min_time_python / min_time_cython
  print('Cython      : {min_time_cython:.4f}s'.format(**locals()) + '{diff_cython:>40,.2f}x'.format(**locals()))

  min_time_nim = nim_fib_rec()
  diff_nim = min_time_python / min_time_nim
  print('Nim         : {min_time_nim:.4f}s'.format(**locals()) + '{diff_nim:>40,.2f}x'.format(**locals()))
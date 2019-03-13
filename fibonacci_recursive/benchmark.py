# importing the required modules
import timeit
import os

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


def runIt():
  print("\nRunning benchmark 'fibonacci_recursive' to {PLACES} places.".format(**globals()))
  print("---------------------------------------------------"+('-'*len(str(PLACES))))

  min_time_python = python_fib_rec()
  print('Pure Python : {min_time_python:.4f}s'.format(**locals()))
  
  min_time_nuitka = nuitka_fib_rec()
  diff_python_nuitka = min_time_python / min_time_nuitka
  print('Nuitka      : {min_time_nuitka:.4f}s'.format(**locals()) + '{diff_python_nuitka:>40,.2f}x'.format(**locals()))
  
  min_time_nim = nim_fib_rec()
  diff_python_nim = min_time_python / min_time_nim
  print('Nim         : {min_time_nim:.4f}s'.format(**locals()) + '{diff_python_nim:>40,.2f}x'.format(**locals()))

if __name__ == "__main__":
  runIt()
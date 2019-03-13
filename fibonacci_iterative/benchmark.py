# importing the required modules
import timeit

PLACES = 100000


def python_fib_iter():
  SETUP_CODE = '''
from Python import fib_iter
  '''

  TEST_CODE = '''
x = fib_iter.fibIter({PLACES})'''.format(**globals())

  # timeit.repeat statement
  times = timeit.repeat(
    setup=SETUP_CODE,
    stmt=TEST_CODE,
    repeat=3,
    number=20
    )

  # printing minimum exec. time
  return min(times)


def nuitka_fib_iter():
  SETUP_CODE = '''
from Nuitka import fib_iter
'''

  TEST_CODE = '''
x = fib_iter.fibIter({PLACES})'''.format(**globals())

  # timeit.repeat statement
  times = timeit.repeat(
    setup=SETUP_CODE,
    stmt=TEST_CODE,
    repeat=3,
    number=20
    )

  # printing minimum exec. time
  return min(times)


def nim_fib_iter():
  SETUP_CODE = '''
from Nim import fib_iter
  '''

  TEST_CODE = '''
x = fib_iter.fibIter({PLACES})'''.format(**globals())

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
  print("\nRunning benchmark 'fibonacci_iterative' to {PLACES} places.".format(**globals()))
  print("---------------------------------------------------"+('-'*len(str(PLACES))))

  min_time_python = python_fib_iter()
  print('Pure Python : {min_time_python:.4f}s'.format(**locals()))
  
  min_time_nuitka = nuitka_fib_iter()
  diff_python_nuitka = min_time_python / min_time_nuitka
  print('Nuitka      : {min_time_nuitka:.4f}s'.format(**locals()) + '{diff_python_nuitka:>40,.2f}x'.format(**locals()))
  
  min_time_nim = nim_fib_iter()
  diff_python_nim = min_time_python / min_time_nim
  print('Nim         : {min_time_nim:.4f}s'.format(**locals()) + '{diff_python_nim:>40,.2f}x'.format(**locals()))
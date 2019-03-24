from numba import jit, int32, int64

@jit((int32, int32))
def myRange(s, e):
  r = list()
  for i in range(s, e):
    r.append(i)
  return r
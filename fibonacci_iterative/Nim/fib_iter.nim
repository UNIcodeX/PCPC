import nimpy

proc fibIter*(n: int64): int64 {.exportpy.} =
  var
    n = n
    a = 0
    b = 1
  while n > 0:
    swap a, b
    a += b
    n -= 1
  result = a

import nimpy

proc fibRec(n: uint64): uint64 {.exportpy.} =
  if n <= 2:
    result = 1
  else:
    result = fibRec(n - 1) + fibRec(n - 2)

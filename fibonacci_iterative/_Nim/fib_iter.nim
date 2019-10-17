import nimpy

proc fibIter*(n: uint64): uint64 {.exportpy.} =
  var
    a = 0'u64
    b = 1'u64
  for i in 0 ..< n:
    swap a, b
    a += b
  result = a

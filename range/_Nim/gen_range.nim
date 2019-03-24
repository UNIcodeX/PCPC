import nimpy

proc myRange*(s, e: int64): seq[int64] {.exportpy.} =
  for i in s .. e:
    result.add i
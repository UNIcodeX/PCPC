import base64, nimpy

{.passL: "-fPIC -shared".}

proc b64e(s: string): string {.exportpy.} = 
  result = base64.encode(s)

proc b64d(s: string): string {.exportpy.} =
  result = base64.decode(s)

when defined(release):
  assert b64d("dGVzdA==") == "test"
  assert b64e("test") == "dGVzdA=="

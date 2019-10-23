import base64

def b64e(str s):
  return base64.b64encode(str(s).encode())

def b64d(bytes s):
  return base64.b64decode(s).decode()
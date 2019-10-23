import base64

def b64e(s):
  return base64.b64encode(str(s).encode())

def b64d(s):
  return base64.b64decode(s).decode()

if __name__ == "__main__":
  assert b64e("test") == b"dGVzdA=="
  assert b64d("dGVzdA==") == "test"
from time import time
from authlib.jose import jwt

# secrets:
# 1 KEY
# 2 SECRET
with open("secrets") as f:
    KEY = f.readline().strip()
    SECRET = f.readline().strip()

HEADER = {
    "alg": "HS256",
    "typ": "JWT"
}


def jwt_token():
    now = int(time())
    tomorrow = now + 86400 * 2
    payload = {
        "appKey": KEY,
        "iat": now,
        "exp": tomorrow,
        "tokenExp": tomorrow
    }
    print("Token follows: ")
    print(jwt.encode(HEADER, payload, key=SECRET).decode("utf-8"))


def info(obj):
    print("Type: " + str(type(obj)))
    print([s for s in dir(obj) if not s.startswith("_")])


jwt_token()

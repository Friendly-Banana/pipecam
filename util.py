from time import time
from authlib.jose import jwt

# secrets: 1 KEY  2 SECRET
with open("secrets") as f:
    KEY = f.readline()
    SECRET = f.readline()

HEADER = {
    "alg": "HS256",
    "typ": "JWT"
}

PAYLOAD = {
    "appKey": "",
    "iat": 0,
    "exp": 0,
    "tokenExp": 0
}


def jwt_token():
    now = int(time())
    tomorrow = now + 86400
    payload = PAYLOAD.copy()
    for data, key in zip(PAYLOAD, (KEY, now, tomorrow, tomorrow)):
        payload[key] = data
    print("Token follows: ")
    print(jwt.encode(HEADER, payload, key=SECRET).decode("utf-8"))


def info(obj):
    print("Type: " + str(type(obj)))
    print([s for s in dir(obj) if not s.startswith("_")])

jwt_token()
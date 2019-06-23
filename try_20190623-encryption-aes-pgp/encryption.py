from Crypto.Cipher import AES
import base64
import os
import sys

def encrytion(privateInfo):
    BLOCK_SIZE = 16
    PADDING = "{"

    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))

    secret = os.urandom(BLOCK_SIZE)
    print("encryption key: ", secret)
    print(len(secret))
    cipher = AES.new(secret)

    encoded = EncodeAES(cipher, privateInfo)
    print("Encrypted string: ", encoded)

print(encrytion("To decode this sentence"))

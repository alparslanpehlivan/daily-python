from Crypto.Cipher import AES
import base64
import os
def decryption(encrytedString):
    PADDING = "{"
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    key = "" #key from encryption.py
    cipher = AES.new(key)
    decoded = DecodeAES(cipher,encrytedString)
    print(decoded)

print(decryption()) #code from encryption.py
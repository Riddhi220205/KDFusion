# encryption.py
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_data(key: bytes, plaintext: bytes):
    nonce = os.urandom(12)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)
    return nonce, ciphertext

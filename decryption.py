# decryption.py
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def decrypt_data(key: bytes, nonce: bytes, ciphertext: bytes):
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(nonce, ciphertext, None)

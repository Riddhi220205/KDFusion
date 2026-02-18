# hybrid_kdf.py
from .argon2_kdf import argon2_kdf
from .hkdf_layer import hkdf_expand

def hybrid_kdf(password: str, salt: bytes) -> bytes:
    ik = argon2_kdf(password, salt)
    return hkdf_expand(ik, b"hybrid-kdf-project")

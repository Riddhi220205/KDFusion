# argon2_kdf.py
from argon2.low_level import hash_secret_raw, Type

def argon2_kdf(password: str, salt: bytes) -> bytes:
    return hash_secret_raw(
        secret=password.encode(),
        salt=salt,
        time_cost=3,
        memory_cost=65536,
        parallelism=2,
        hash_len=32,
        type=Type.ID
    )

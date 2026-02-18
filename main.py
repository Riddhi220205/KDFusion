from salt_generator import generate_salt
from hybrid_kdf import hybrid_kdf
from encryption import encrypt_data
from decryption import decrypt_data
import getpass

def main():
    # User input
    password = getpass.getpass("Enter password: ")
    data = input("Enter data to encrypt: ").encode()

    # Generate salt
    salt = generate_salt()

    # Derive key using Hybrid KDF
    key = hybrid_kdf(password, salt)

    # Encrypt
    nonce, encrypted = encrypt_data(key, data)

    # Decrypt
    key_for_decryption = hybrid_kdf(password, salt)
    decrypted = decrypt_data(key_for_decryption, nonce, encrypted)

    print("\nEncrypted:", encrypted)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    main()

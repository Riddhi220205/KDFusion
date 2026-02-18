KDFusion: Hybrid Cryptographic Key Derivation Framework

## Overview

KDFusion is a modular cryptographic backend framework that analyzes the security of Key Derivation Functions (KDFs) combined with a hybrid cryptographic approach.

The system integrates:

- Elliptic Curve Diffie–Hellman (ECDH) for secure key exchange
- HKDF for entropy extraction and key expansion
- Argon2 and PBKDF2 for password-based key derivation
- AES-256 for symmetric encryption

This project evaluates security properties, performance metrics, and attack resistance of modern KDF mechanisms in hybrid architectures.

---

## Objectives

- Implement hybrid key exchange and derivation model
- Compare multiple KDFs (HKDF, PBKDF2, Argon2)
- Analyze brute-force resistance and entropy strength
- Measure computational cost and performance
- Demonstrate secure AES-based encryption workflow

---

## Architecture

Client/Server Key Exchange:
1. ECDH generates shared secret
2. Shared secret passed to HKDF
3. HKDF derives session key
4. AES-256 encrypts application data

Password-Based Flow:
1. User password + salt
2. Argon2 or PBKDF2 derives key
3. Derived key used for AES encryption

---

## Project Structure
kdf/
│
├── argon2_kdf.py
├── hkdf_layer.py
├── hybrid_kdf.py
├── encryption.py
├── decryption.py
├── salt_generator.py
├── main.py
└── README.md


---

## Implemented Cryptographic Components

- Argon2 (memory-hard password hashing)
- PBKDF2 (iteration-based KDF)
- HKDF (HMAC-based key derivation)
- AES-256 (symmetric encryption)
- Secure random salt generation

---

## Security Analysis Highlights

- Salt-based defense against rainbow table attacks
- Adjustable iteration count for brute-force resistance
- Memory hardness evaluation (Argon2)
- Key separation via HKDF extract-and-expand model
- Forward secrecy through ECDH-based hybrid approach

---

## Performance Evaluation

The system supports benchmarking of:

- Execution time vs iteration count
- Memory cost impact (Argon2)
- KDF comparison metrics
- Encryption/decryption latency

---

## Installation

Clone the repository:

git clone https://github.com/Riddhi220205/KDFusion.git
cd KDFusion

Install dependencies:

pip install -r requirements.txt

---

## Running the Project

python main.py
---

## Future Enhancements

- Web-based dashboard for KDF comparison
- Automated attack cost estimator
- GPU-resistance benchmarking
- Dockerized deployment

---

## Technologies Used

- Python 3.x
- Cryptography library
- Argon2-cffi
- hashlib

---

## Author

Riddhi Vatsala 

Cryptography & Security Engineering Project

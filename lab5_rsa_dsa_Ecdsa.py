# Install the cryptography library if not already installed
# Command: pip install cryptography

from cryptography.hazmat.primitives.asymmetric import rsa, dsa, ec, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def generate_RSA_key_pair():
    """Generate RSA key pair."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_RSA(public_key, plaintext):
    """Encrypt plaintext with RSA public key."""
    ciphertext = public_key.encrypt(
        plaintext,
        padding.PKCS1v15()
    )
    return ciphertext

def decrypt_RSA(private_key, ciphertext):
    """Decrypt ciphertext with RSA private key."""
    plaintext = private_key.decrypt(
        ciphertext,
        padding.PKCS1v15()
    )
    return plaintext

def generate_DSA_key_pair():
    """Generate DSA key pair."""
    private_key = dsa.generate_private_key(
        key_size=1024,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign_DSA(private_key, message):
    """Sign message with DSA private key."""
    signature = private_key.sign(
        message,
        hashes.SHA256()
    )
    return signature

def verify_DSA(public_key, message, signature):
    """Verify DSA signature."""
    try:
        public_key.verify(
            signature,
            message,
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

def generate_ECDSA_key_pair():
    """Generate ECDSA key pair."""
    private_key = ec.generate_private_key(
        ec.SECP256R1(),
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign_ECDSA(private_key, message):
    """Sign message with ECDSA private key."""
    signature = private_key.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )
    return signature

def verify_ECDSA(public_key, message, signature):
    """Verify ECDSA signature."""
    try:
        public_key.verify(
            signature,
            message,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except Exception:
        return False

def main():
    # RSA Operations
    rsa_private_key, rsa_public_key = generate_RSA_key_pair()
    plaintext = b"Message for RSA algorithm"
    ciphertext = encrypt_RSA(rsa_public_key, plaintext)
    decrypted_text = decrypt_RSA(rsa_private_key, ciphertext)
    
    print("RSA Public Key:", rsa_public_key)
    print("RSA Private Key:", rsa_private_key)
    print("Plaintext:", plaintext.decode())
    print("Ciphertext:", ciphertext)
    print("Decrypted Text:", decrypted_text.decode())
    
    # DSA Operations
    dsa_private_key, dsa_public_key = generate_DSA_key_pair()
    message = b"Message for DSA algorithm"
    signature = sign_DSA(dsa_private_key, message)
    verified = verify_DSA(dsa_public_key, message, signature)
    
    print("DSA Public Key:", dsa_public_key)
    print("DSA Private Key:", dsa_private_key)
    print("Message:", message.decode())
    print("Signature:", signature)
    print("Verification:", verified)
    
    # ECDSA Operations
    ecdsa_private_key, ecdsa_public_key = generate_ECDSA_key_pair()
    ecdsa_signature = sign_ECDSA(ecdsa_private_key, message)
    ecdsa_verified = verify_ECDSA(ecdsa_public_key, message, ecdsa_signature)
    
    print("ECDSA Public Key:", ecdsa_public_key)
    print("ECDSA Private Key:", ecdsa_private_key)
    print("ECDSA Signature:", ecdsa_signature)
    print("ECDSA Verification:", ecdsa_verified)

# Simplified main function call
main()

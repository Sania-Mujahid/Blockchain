import base64
import cryptography
# We need these libraries to handle cryptography, hashing, and encoding
from cryptography.hazmat.primitives.asymmetric import ec  # For ECDSA keys
from cryptography.hazmat.primitives import serialization  # To convert keys to bytes
import hashlib  # For hashing (SHA-256 and RIPEMD-160)
import base58  # For encoding the final Bitcoin address
# Function to generate an ECDSA private key and its corresponding public key
def generate_keys():
    # Generate private key using the SECP256K1 curve (used by Bitcoin)
    private_key = ec.generate_private_key(ec.SECP256K1())
    
    # Get the public key from the private key
    public_key = private_key.public_key()
    
    # Return both keys (private and public)
    return private_key, public_key
# Function to convert a public key to a Bitcoin wallet address
def public_key_to_address(public_key):
    # Convert the public key to bytes (uncompressed format) so we can hash it
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.X962,  # Standard encoding for public keys
        format=serialization.PublicFormat.UncompressedPoint  # Uncompressed point format
    )
    
    # Step 1: Perform SHA-256 hashing on the public key bytes
    sha256_hash = hashlib.sha256(public_key_bytes).digest()
    
    # Step 2: Perform RIPEMD-160 hashing on the SHA-256 hash (to get the Bitcoin address format)
    ripemd160 = hashlib.new('ripemd160')  # Create a new RIPEMD-160 hashing object
    ripemd160.update(sha256_hash)  # Hash the SHA-256 hash
    hashed_public_key = ripemd160.digest()  # Get the final RIPEMD-160 hash
    
    # Step 3: Add version byte (0x00 for main Bitcoin network)
    versioned_payload = b'\x00' + hashed_public_key
    
    # Step 4: Create checksum by hashing the versioned payload twice with SHA-256
    checksum = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()[:4]
    
    # Step 5: Append the checksum to the versioned payload
    final_payload = versioned_payload + checksum
    
    # Step 6: Encode the final payload into a Bitcoin address using Base58 encoding
    address = base58.b58encode(final_payload).decode('utf-8')
    
    return address  # Return the Bitcoin wallet address

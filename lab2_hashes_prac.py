import hashlib  # Import the hashlib module for various hash functions
import bcrypt  # Import the bcrypt module for bcrypt hashing

name = "sania_dewaan"  # Define the string to be hashed

# Calculate MD5 hash
md5_hash = hashlib.md5(name.encode('utf-8')).hexdigest()
# Convert the string to bytes, compute the MD5 hash, and get its hexadecimal representation
print("md5:", md5_hash)  # Print the MD5 hash

# Calculate SHA-1 hash
sha1_hash= hashlib.sha1(name.encode()).hexdigest()
# Convert the string to bytes, compute the SHA-1 hash, and get its hexadecimal representation
print("sha1:", sha1_hash)  # Print the SHA-1 hash

try:
    # Calculate RIPEMD-160 hash
    ripemd160_hash = hashlib.new('ripemd160', name.encode()).hexdigest()
    # Convert the string to bytes, compute the RIPEMD-160 hash, and get its hexadecimal representation
    print("ripe-160:", ripemd160_hash)  # Print the RIPEMD-160 hash
except ValueError:
    # Handle the case where RIPEMD-160 is not supported by hashlib
    print("ripemd160 is not supported by hashlib.")  # Print an error message if RIPEMD-160 is not supported

# Calculate bcrypt hash
bcrypt_hash = bcrypt.hashpw(name.encode(), bcrypt.gensalt())
# Compute the bcrypt hash of the string with a generated salt
print("bcrypt:", bcrypt_hash.decode())  # Print the bcrypt hash (decoded from bytes to string)

# Calculate SHA-256 hash
sha256_hash = hashlib.sha256(name.encode()).hexdigest()
# Convert the string to bytes, compute the SHA-256 hash, and get its hexadecimal representation
print("sha256:", sha256_hash)  # Print the SHA-256 hash

# Calculate SHA-512 hash
sha512_hash = hashlib.sha512(name.encode()).hexdigest()
# Convert the string to bytes, compute the SHA-512 hash, and get its hexadecimal representation
print("sha512:", sha512_hash)  # Print the SHA-512 hash

# Calculate BLAKE2b hash
blake2_hash = hashlib.blake2b(name.encode()).hexdigest()
# Convert the string to bytes, compute the BLAKE2b hash, and get its hexadecimal representation
print("BLAKE2b:", blake2_hash)  # Print the BLAKE2b hash

# Calculate SHA-3-256 hash
sha3_256_hash = hashlib.sha3_256(name.encode()).hexdigest()
# Convert the string to bytes, compute the SHA-3-256 hash, and get its hexadecimal representation
print("SHA-3-256:", sha3_256_hash)  # Print the SHA-3-256 hash

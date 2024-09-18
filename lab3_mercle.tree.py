import hashlib

def sha256(data):
    """Return the SHA-256 hash of the given data."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()
def combine_and_hash(hash1, hash2):
    """Combine two hashes and return their SHA-256 hash."""
    combined = hash1 + hash2
    return sha256(combined)

# Text parts provided
part1 = "And now the end is here..."
part2 = "Regrets, I've had a few..."
part3 = "Yes, there were times I'm sure you knew..."
part4 = "For what is a man, what has he got?"

# Calculate the SHA-256 hashes for each part
hash1 = sha256(part1)
hash2 = sha256(part2)
hash3 = sha256(part3)
hash4 = sha256(part4)

print("Hash of Part 1:", hash1)
print("Hash of Part 2:", hash2)
print("Hash of Part 3:", hash3)
print("Hash of Part 4:", hash4)

# Combine and hash the pairs
hash12 = combine_and_hash(hash1, hash2)
hash34 = combine_and_hash(hash3, hash4)

print("Combined Hash of Part 1 and Part 2:", hash12)
print("Combined Hash of Part 3 and Part 4:", hash34)

# Combine the resulting hashes to get the Merkle Root
merkle_root = combine_and_hash(hash12, hash34)

print("Merkle Root:", merkle_root)

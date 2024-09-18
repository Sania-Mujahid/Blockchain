import hashlib  # Import hashlib for hashing

# Function to calculate the SHA-256 hash of a string
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Function to combine two hashes and return their SHA-256 hash
def combine_and_hash(hash1, hash2):
    return sha256(hash1 + hash2)

# Step 1: Take eight random strings
strings = [
    "apple", "banana", "cherry", "date",
    "elderberry", "fig", "grape", "honeydew"
]

# Step 2: Calculate the SHA-256 hashes for each string individually
hash1 = sha256(strings[0])
hash2 = sha256(strings[1])
hash3 = sha256(strings[2])
hash4 = sha256(strings[3])
hash5 = sha256(strings[4])
hash6 = sha256(strings[5])
hash7 = sha256(strings[6])
hash8 = sha256(strings[7])

# Print each hash
print("Hash of String 1:", hash1)
print("Hash of String 2:", hash2)
print("Hash of String 3:", hash3)
print("Hash of String 4:", hash4)
print("Hash of String 5:", hash5)
print("Hash of String 6:", hash6)
print("Hash of String 7:", hash7)
print("Hash of String 8:", hash8)

# Combine and hash the pairs to build the Merkle tree
hash12 = combine_and_hash(hash1, hash2)
hash34 = combine_and_hash(hash3, hash4)
hash56 = combine_and_hash(hash5, hash6)
hash78 = combine_and_hash(hash7, hash8)

# Print combined hashes
print("Combined Hash of String 1 and 2:", hash12)
print("Combined Hash of String 3 and 4:", hash34)
print("Combined Hash of String 5 and 6:", hash56)
print("Combined Hash of String 7 and 8:", hash78)

# Combine and hash the results from previous steps
hash1234 = combine_and_hash(hash12, hash34)
hash5678 = combine_and_hash(hash56, hash78)

# Print combined hashes
print("Combined Hash of (1-2) and (3-4):", hash1234)
print("Combined Hash of (5-6) and (7-8):", hash5678)

# Final combination to get the Merkle root
merkle_root = combine_and_hash(hash1234, hash5678)

# Print the Merkle root
print("Merkle Root:", merkle_root)

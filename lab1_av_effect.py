import hashlib

# Function to hash a single string
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Function to combine two hashes and return their hash
def combine_hashes(hash1, hash2):
    return hashlib.sha256(hash1 + hash2)

# Input strings
string1 = "my name is sania dewaan"
string2 = "my father name is mujahid"
string3 = "i am student of blockchain"
string4 = "curently i am doing BS from KIU"

# Step 1: Hash the input strings
hash1 = hashlib.sha256(string1.encode()).hexdigest()
hash2 = hashlib.sha256(string2.encode()).hexdigest()
hash3 = hashlib.sha256(string3.encode()).hexdigest
hash4 = hashlib.sha256(string4.encode).hexdigest()
print("hash of string1:\n",hash1)
print("hash of string2:\n",hash2)
print("hash of string3:\n",hash3)
print("hash of string4:\n",hash4)

# Step 2: Combine the hashes in pairs
combined_hash1 = combine_hashes(hash1, hash2)
combined_hash2 = combine_hashes(hash3, hash4)
print("the combined hash of string1 and string2 is:\n",combined_hash1)
print("the combined hash of string3 and string4 is:\n",combined_hash2)

# Step 3: Combine the resulting hashes to get the final Merkle root
merkle_root = combine_hashes(combined_hash1, combined_hash2)

# Print the final Merkle root
print("Merkle Root:", merkle_root)

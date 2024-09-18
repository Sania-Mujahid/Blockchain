import hashlib

# Function to create a SHA-256 hash from data
def make_hash(data):
    return hashlib.sha256(data).hexdigest()

# Function to combine two hashes and return their SHA-256 hash
def combine_and_hash(hash1, hash2):
    combined = hash1 + hash2
    return make_hash(combined.encode('utf-8'))

# Read the file and split it into blocks of 1024 bytes
def read_file(filename, block_size=1024):
    pieces = []
    with open(filename, 'rb') as file:
        while True:
            block = file.read(block_size)
            if not block:
                break
            pieces.append(block)
    return pieces

# Main code
filename = '1.1-introduction-to-the-course.txt'  # Replace with your file path
pieces = read_file(filename)

# Calculate and print the hash for each block
hashes = []
for piece in pieces:
    hash_value = make_hash(piece)
    hashes.append(hash_value)
    print(f"Hash for Block {len(hashes)}: {hash_value}")

# Combine hashes until only one hash (Merkle root) is left
while len(hashes) > 1:
    new_hashes = []
    for i in range(0, len(hashes) - 1, 2):
        combined_hash = combine_and_hash(hashes[i], hashes[i + 1])
        new_hashes.append(combined_hash)
    hashes = new_hashes

# Print the final hash (Merkle Root)
if hashes:
    print("Merkle Root:", hashes[0])
else:
    print("No Merkle root.")

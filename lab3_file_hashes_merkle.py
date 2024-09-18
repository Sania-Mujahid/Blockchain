import hashlib  # Import hashlib for hashing

# Function to calculate the SHA-256 hash of a string
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Read the file and get the first 8 lines as blocks
filename = '1.1-Introduction-to-the-Course.txt'  # Replace with your file path
try:
    with open(filename, 'r', encoding='utf-8') as file:  # Specify UTF-8 encoding
        lines = file.readlines()
except UnicodeDecodeError:
    print("Error: Could not decode the file. Please check the file encoding.")
    exit()

# Take only the first 8 lines
blocks = [line.strip() for line in lines[:8]]

# Calculate SHA-256 hashes for each block and print them
if len(blocks) >= 8:
    hash1 = sha256(blocks[0])
    print("Hash of Block 1:", hash1)

    hash2 = sha256(blocks[1])
    print("Hash of Block 2:", hash2)

    hash3 = sha256(blocks[2])
    print("Hash of Block 3:", hash3)

    hash4 = sha256(blocks[3])
    print("Hash of Block 4:", hash4)

    hash5 = sha256(blocks[4])
    print("Hash of Block 5:", hash5)

    hash6 = sha256(blocks[5])
    print("Hash of Block 6:", hash6)

    hash7 = sha256(blocks[6])
    print("Hash of Block 7:", hash7)

    hash8 = sha256(blocks[7])
    print("Hash of Block 8:", hash8)

    # Combine pairs of hashes to form the Merkle tree
    hash12 = sha256(hash1 + hash2)
    hash34 = sha256(hash3 + hash4)
    hash56 = sha256(hash5 + hash6)
    hash78 = sha256(hash7 + hash8)

    # Combine the results to get the final Merkle root
    final_hash1 = sha256(hash12 + hash34)
    final_hash2 = sha256(hash56 + hash78)
    merkle_root = sha256(final_hash1 + final_hash2)

    # Print the Merkle root
    print("Merkle Root:", merkle_root)
else:
    print("Not enough blocks found in the file.")

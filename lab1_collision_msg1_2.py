import hashlib

# Define a function to calculate hash values
def calculate_hash(file_path, hash_function):
    with open(file_path, "rb") as file:
        file_data = file.read()
        hash_object = hash_function(file_data)
        return hash_object.hexdigest()

# File paths
file1 = "message1.bin"
file2 = "message2.bin"

# Calculate MD5 and SHA-1 for both files
md5_file1 = calculate_hash(file1, hashlib.md5)
md5_file2 = calculate_hash(file2, hashlib.md5)

sha1_file1 = calculate_hash(file1, hashlib.sha1)
sha1_file2 = calculate_hash(file2, hashlib.sha1)

# Print the results
print(f"MD5 of {file1}: {md5_file1}")
print(f"MD5 of {file2}: {md5_file2}")
print(f"SHA-1 of {file1}: {sha1_file1}")
print(f"SHA-1 of {file2}: {sha1_file2}")

# Check for collisions
if md5_file1 == md5_file2:
    print("MD5 collision detected!")
else:
    print("No MD5 collision.")

if sha1_file1 == sha1_file2:
    print("SHA-1 collision detected!")
else:
    print("No SHA-1 collision.")
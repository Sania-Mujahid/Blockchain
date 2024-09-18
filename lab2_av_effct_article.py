import hashlib

def calculate_ripemd160_hash(text):
    """
    Calculate the RIPEMD-160 hash of a string.

    Args:
    text (str): The string to hash.

    Returns:
    str: The hexadecimal digest of the hash.
    """
    # Convert the string to bytes
    text_bytes = text.encode()
    # Calculate the RIPEMD-160 hash
    hash_object = hashlib.new('ripemd160', text_bytes)
    return hash_object.hexdigest()

# Read the article from a file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Read the original article
original_text = read_file('article.txt')
print("Original Hash (RIPEMD-160):", calculate_ripemd160_hash(original_text))

# Modify the article text slightly
modified_text = original_text + " This is a small change."
print("Modified Hash (RIPEMD-160):", calculate_ripemd160_hash(modified_text))

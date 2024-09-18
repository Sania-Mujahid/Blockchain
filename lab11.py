import hashlib
# Inputs
sender = input("Enter sender's email: ")
recipient = input("Enter recipient's email: ")
subject = input("Enter the subject of the email: ")
message = input("Enter the message body: ")
nonce = int(input("Enter the nonce: "))
#ouput statements
print(sender)
print(recipient)
print(subject)
print(message)
print(nonce)
#initialize nonce with 0
nonce=0
counter=0
#variable string_catcatenate to combine all inputs except nonce
string_catcatenate=sender+recipient+subject+message
#show catcatenation result
print(string_catcatenate)
#condion will be check untill it false
while True:
    #add nonce with catcatenated inputs
    str_catecatenate_nonce=string_catcatenate+str(nonce)
    #hash of currently catcatenated string with nonce stored in current_str_hash
    current_str_hash=hashlib.sha256(str_catecatenate_nonce.encode()).hexdigest()
    #condion if trure hash will be ouput
    if current_str_hash.startswith("ff"):
        print("hash found:",current_str_hash)


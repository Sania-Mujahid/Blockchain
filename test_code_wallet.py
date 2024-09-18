'''
Title - Hello Bitcoin Bee
This program demonstrates the creation of - private key, - public key - and a bitcoin address.
'''
#This library allows you to connect to the Bitcoin network and pull data from places such as Blockchain.info. Let’s start with a Hello World program for Bitcoin in Python. In the hello_bitcoin.py script, the demonstration of a new bitcoin address is created using Python.
#pip install bitcoin
# import bitcoin
from bitcoin import *
#Follow the below steps to run the program using python
#Import the bitcoin library
# import bitcoin
from bitcoin import *
#Generate a private key using the random key function:
my_private_key = random_key()
#Display the private key on the screen:

print("Private Key: %s\n" % my_private_key)
# Generate Public Key
my_public_key = privtopub(my_private_key)
print("Public Key: %s\n" % my_public_key)
# Create a bitcoin address
my_bitcoin_address = pubtoaddr(my_public_key)
print("Bitcoin Address: %s\n" % my_bitcoin_address)

import hashlib
import datetime

def hashify(stringToHash):
	'''Use this to encode a string of text into a hash.'''
	hashbrown = hashlib.sha256()
	hashbrown.update(str(stringToHash).encode('utf-8'))
	return hashbrown.hexdigest()

def basicDriver():
	'''Makes the file usable'''
	string = str(input("Please enter a string:"))
	print("Hashbrown done! Grab it here! :" +hashify(string))

basicDriver()
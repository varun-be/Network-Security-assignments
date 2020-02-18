import os
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

key = 3
path = '/home/pc/test'

fileList = os.listdir(path)
for i in fileList:
	f=open(os.path.join(path,i), "r")
	plaintext = f.read()
	#print(plaintext)
	
# encipher
	ciphertext = ""
	for c in plaintext.upper():
		if c.isalpha(): ciphertext += I2L[ (L2I[c] + key)%26 ]
		else: ciphertext += c
	f=open(os.path.join(path,i), "w+")
	f.write(ciphertext)

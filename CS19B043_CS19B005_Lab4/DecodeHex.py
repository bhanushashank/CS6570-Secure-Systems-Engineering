import os

def decode(s):
	hexcodes = {'0': 0, '1': 1, '2': 2,'3': 3, '4': 4, '5': 5,
		    '6': 6, '7': 7, '8': 8,'9': 9, 'a': 10, 
 		    'b': 11,'c': 12, 'd': 13, 'e': 14,'f': 15 }
	
	output = ""
	if(s[0] == '%'):
		return ""
	for i in range(0, len(s), 2):
		hexa = 16*hexcodes[s[i]] + hexcodes[s[i+1]]
		output += chr(hexa)
	return output

file1 = open("dump.txt","r")
lines = file1.readlines()
file1.close()

decoded_string = ""

for line in lines:
	l = line.strip().split(" ")
	if(len(l) > 4):
		hexa = decode(l[4])
		print
		decoded_string += hexa[::-1]
		
file2 = open("DecodedStack.txt", "a")
file2.write(decoded_string)
file2.close()
print("Run SearchPasswords.py to search for potential passwords")


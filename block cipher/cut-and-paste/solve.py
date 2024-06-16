from pwn import *
#user:KasuganoSor  ->block 1 -> 0~15
#a;padding:aaaaaa  ->block 2 -> 16~31
#aaaaaaaaa;favora  ->block 3 -> 32~47
#bility:90000000;  ->block 4 -> 48~63
#favorability:0;   ->block 5 -> 64~79

#payload:
#aaaaaaaaaaaaaaa;favorability:90000000;

r=remote('ctf.ckcsc.net',60002)
r.sendline(b'2')
r.sendline(b'aaaaaaaaaaaaaaa;favorability:90000000;')
r.recvuntil(b'=')
token=bytes.fromhex(r.recvline().strip().split(b"=")[1].decode())
print(token)

#0~63
token=token[:64]

r.sendlineafter('token = ', token.hex())
r.sendline(b"Y")

r.interactive()
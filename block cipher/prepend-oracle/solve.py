import string
from pwn import *

r = remote('ctf.ckcsc.net', 60003)

r.sendline(b'2')


def oracle(m):
    r.sendlineafter(b'message = ', m.hex())
    return bytes.fromhex(r.recvline().strip().partition(b' = ')[2].decode())

flag = b''
for i in range(100):
    
    prefix = b'A' * (48 - 1 - i)
    target = oracle(prefix)[:48]
    for c in string.printable:
        test = oracle(prefix + flag + bytes([ord(c)]))[:48]
        if test == target:
            flag += bytes([ord(c)])
            print(flag)
            break

r.interactive()
#AAA..
#AAA..
#aaaaaaaaaaaaaa
from pwn import *
r=remote('ctf.ckcsc.net' , 60004)

r.sendline(b'1')
r.recvuntil(":")
ciphertext=base64.b64decode(r.recvline().strip().decode()[2:][:-1])

plaintext = "ABCDEFGHIJKLMNOP1234567890abcdef"

IV = bytearray(ciphertext[:16])
C = ciphertext[16:]

IV[0] = IV[0] ^ ord(plaintext[0]) ^ ord('H')

CIPHER = bytes(IV) + C
print("change=",CIPHER.hex())
r.sendline(b'2')
r.sendlineafter(b'Your Cipher= ',CIPHER.hex())

r.interactive()

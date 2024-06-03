from pwn import *
r=remote('ctf.ckcsc.net' ,60000)
for i in range(100):
    round=r.recvline()
    print(round)
    r.recvline()
    g=r.recvline()
    a=g.strip().split(b"\x9a")[1]
    ans=eval(a.decode())
    r.sendline(str(ans).encode())
    r.recvline()
    r.recvline()
r.interactive()



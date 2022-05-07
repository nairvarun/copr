def fib(a, b):
    s = 2
    c = 0
    while c < 4000000:
        c = a + b
        if c % 2 == 0:
            s += c
        a = b
        b = c
    return s

print(fib(1, 2))

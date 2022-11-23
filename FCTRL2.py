def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * f(n-1)

n = int(input())

for i in range(n):
    num = int(input())
    print(f(num))

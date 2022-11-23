for i in range(int(input())):
    n = 0
    a, b = map(int, input().split())
    for i in range(a, b+1):
        if str(i)[-1] == '2' or str(i)[-1] == '3' or str(i)[-1] == '9':
            n += 1
    print(n)

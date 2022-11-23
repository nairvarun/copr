for i in range(int(input())):
    ans = 0
    n, h = map(int, input().split())
    a = map(int, input().split())
    for i in a:
        if i > h:
            ans += 1
    print(ans)

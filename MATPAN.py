for _ in range(int(input())):
    d = dict(zip(list(map(chr, range(97, 123))), map(int, input().split())))
    s = set()
    for i in input(): s.add(i)
    ans = 0
    for i in d.keys()-s: ans += d[i]
    print(ans)

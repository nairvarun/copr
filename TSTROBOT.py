from collections import Counter
for _ in range(int(input())):
    c, s = map(int, input().split())
    p = input()
    q = {s}
    for i in p:
        if i == 'R':
            q.add(s:=s+1)
        else:
            q.add(s:=s-1)
    print(len(q))

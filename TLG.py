n = int(input())
maxlead = p1 = p2 = p = 0
for i in range(n):
    a, b = map(int, input().split())
    p1 += a
    p2 += b
    if p1 > p2:
        lead = p1 - p2
        if lead > maxlead:
            maxlead = lead
            p = 1
    else:
        lead = p2 - p1
        if lead > maxlead:
            maxlead = lead
            p = 2
print(p, maxlead)

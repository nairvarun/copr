from collections import Counter

for _ in range(int(input())):
    _ = input()
    s = input().split()
    cntr = Counter(s)
    if len(cntr) == 1 or cntr.most_common()[0][1] != cntr.most_common()[1][1]:
        print('YES')
    else:
        print('NO')

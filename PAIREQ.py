from collections import Counter

for i in range(int(input())):
    l = int(input())
    a = list(map(int, input().split()))
    print(l - Counter(a).most_common()[0][1])

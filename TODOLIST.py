t = int(input())
for i in range(t):
    n = int(input())
    d = list(map(int, input().split()))
    print(len(list(filter(lambda x: x >= 1000, d))))

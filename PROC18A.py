for i in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(max([sum(a[i:i+k]) for i in range(len(a))]))

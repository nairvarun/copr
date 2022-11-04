from itertools import permutations

n = int(input())
k = int(input())

# n, k = map(int, input().split())

for i in range(n):
    l = list(map(int, input().split()))
    # print(l)
    perms = [i for j in range(1, len(l)+1) for i in permutations(l, j) if all(i[k] <= i[k+1] for k in range(len(i)-1))]
    print(perms)
    print('>>' + str(len(perms)))

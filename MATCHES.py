c = {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6
}
for _ in range(int(input())):
    ans = 0
    s = sum(map(int, input().split()))
    for i in str(s):
        ans += c[i]
    print(ans)

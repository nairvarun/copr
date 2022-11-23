for _ in range(int(input())):
    _ = input()
    s = set(input().split())
    if '0' in s: s.remove('0')
    print(len(s))

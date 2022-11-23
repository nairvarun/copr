for _ in range(int(input())):
    _ = input()
    s = input().split()
    impostors = set()
    for i in range(len(s)-1):
        if s[i] != s[i+1]: impostors |= {i, i+1}
    print(len(impostors))

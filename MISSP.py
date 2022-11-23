for _ in range(int(input())):
    l = []
    for _ in range(int(input())):
        inp = int(input())
        if inp not in l:
            l.append(inp)
        else:
            l.remove(inp)
    print(*l, sep='\n')

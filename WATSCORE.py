for _ in range(int(input())):
    scores = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
    }
    for _ in range(int(input())):
        c, s = map(int, input().split())
        if scores[c] < s:
            scores[c] = s

    score = 0
    for i in range(1, 9):
        score += scores[i]

    print(score)

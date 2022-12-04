from requests import get
from _AOCcookies import cookies

input = get('https://adventofcode.com/2022/day/2/input', cookies=cookies).text

# rock(A)[1] > scissor(Z)[3]
# paper(B)[2] > rock(X)[1]
# scissor(C)[3] > paper(Y)[2]

mv_wt = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

# part one
def calc_score1(x:str) -> int:
    p, q = x[0], x[-1]
    if (p == 'A' and q == 'X') or (p == 'B' and q == 'Y') or (p == 'C' and q == 'Z'):           # draw
        return 3 + mv_wt[q]
    elif (p == 'A' and q == 'Z') or (p == 'B' and q == 'X') or (p == 'C' and q == 'Y'):         # lose
        return 0 + mv_wt[q]
    else:                                                                                       # win
        return 6 + mv_wt[q]

print(sum([calc_score1(i) for i in input.rstrip('\n').split('\n')]))

# part two
mu = {
    'A': {
        'X': 3,
        'Y': 1,
        'Z': 2
    },
    'B': {
        'X': 1,
        'Y': 2,
        'Z': 3
    },
    'C': {
        'X': 2,
        'Y': 3,
        'Z': 1
    }
}

res_wt = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

def calc_score2(x:str) -> int:
    p, q = x[0], x[-1]
    return res_wt[q] + mu[p][q]

print(sum([calc_score2(i) for i in input.rstrip('\n').split('\n')]))

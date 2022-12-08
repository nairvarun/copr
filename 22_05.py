from requests import get
from _AOCcookies import cookies

inp = get('https://adventofcode.com/2022/day/5/input', cookies=cookies).text

crate_state = [list(map(lambda x: x[1], filter(lambda x: x != '   ', x))) for x in [[x[k] for x in map(lambda x: [x[i+1:i+4] for i in range(-1, len(x), 4)], reversed(inp.split('\n')[:8]))] for k in range(9)]]
moves = list(map(lambda x: list(map(int, x.replace('move ', '').replace('from ', '').replace('to ', '').split())), inp.rstrip('\n').split('\n')[10:]))

# part one
for m in moves:
    for _ in range(m[0]):
        crate_state[m[2]-1].append(crate_state[m[1]-1].pop())

print(''.join([x[-1] for x in crate_state]))

# part two
for m in moves:
    crate_state[m[2]-1] += crate_state[m[1]-1][-m[0]:]
    crate_state[m[1]-1] = crate_state[m[1]-1][:-m[0]]

print(''.join([x[-1] for x in crate_state]))

from requests import get
from _AOCcookies import cookies
import string

input = get('https://adventofcode.com/2022/day/3/input', cookies=cookies).text

p = dict((j, i) for i, j in enumerate(string.ascii_letters, 1))

# part one
print(sum([p[k.pop()] for k in [set(j[0]).intersection(set(j[1])) for j in [(i[:len(i)//2], i[len(i)//2:]) for i in input.rstrip('\n').split('\n')]]]))

# part two
e = input.rstrip('\n').split('\n')
print(sum([p[k.pop()] for k in [set(i[0]).intersection(set(i[1])).intersection(set(i[-1])) for i in [e[n:n+3] for n in range(0, len(e), 3)]]]))

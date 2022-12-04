from requests import get
from _cookies import cookies

# part one
print(max([sum(map(int, i.split('\n'))) for i in get('https://adventofcode.com/2022/day/1/input', cookies=cookies).text.rstrip('\n').split('\n\n')]))

# part two
print(sum(sorted([sum(map(int, i.split('\n'))) for i in get('https://adventofcode.com/2022/day/1/input', cookies=cookies).text.rstrip('\n').split('\n\n')])[-3:]))

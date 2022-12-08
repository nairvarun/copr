from requests import get
from _AOCcookies import cookies

input = get('https://adventofcode.com/2022/day/4/input', cookies=cookies).text

# part one
print(len(list(filter(lambda x: (int(x[0][0]) <= int(x[1][0]) and int(x[0][1]) >= int(x[1][1])) or (int(x[0][0]) >= int(x[1][0]) and int(x[0][1]) <= int(x[1][1])), [[j[0].split('-'), j[1].split('-')] for j in [i.split(',') for i in input.rstrip('\n').split('\n')]]))))

# part two
print(len(list(filter(lambda x: (int(x[0][1]) >= int(x[1][0]) and int(x[0][0]) <= int(x[1][0])) or (int(x[1][1]) >= int(x[0][0]) and int(x[1][0]) <= int(x[0][0])), [[j[0].split('-'), j[1].split('-')] for j in [i.split(',') for i in input.rstrip('\n').split('\n')]]))))

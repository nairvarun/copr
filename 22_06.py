from requests import get
from _AOCcookies import cookies

inp = get('https://adventofcode.com/2022/day/6/input', cookies=cookies).text.rstrip('\n')

# part one
for i in range(len(inp)-3):
    if len(set(inp[i:i+4])) == 4:
        print(i+4)
        break

# part two
for i in range(len(inp)-13):
    if len(set(inp[i:i+14])) == 14:
        print(i+14)
        break

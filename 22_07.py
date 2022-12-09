from requests import get
from _AOCcookies import cookies

inp = get('https://adventofcode.com/2022/day/7/input', cookies=cookies).text.rstrip('\n')

dir_map = {
    '/': {
        'lvl': 0,
        'size': 0
    }
}

# part one
curr_lvl = 0
for i in inp.split('\n'):
    if i[:4] == '$ cd':
        if i[5:] == '..':
            curr_lvl = max(0, curr_lvl-1)
        elif i[5:] in dir_map:
            curr_lvl = dir_map[i[5:]]['lvl']
        else:
            curr_lvl += 1
            dir_map[i[5:]] = {
                'lvl': curr_lvl,
                'size': 0
            }

pp(dir_map)

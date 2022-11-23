from collections import Counter
from math import ceil
for _ in range(int(input())):
    s = input()
    if Counter(s[:len(s)//2]) == Counter(s[ceil(len(s)/2):]):
        print('YES')
    else:
        print('NO')

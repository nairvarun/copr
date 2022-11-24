from datetime import datetime

sun = 0
for yr in range(1901, 2001):
    for mnth in range(1, 13):
        if datetime(yr, mnth, 1).weekday() == 6: sun += 1
print(sun)

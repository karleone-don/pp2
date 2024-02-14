import datetime
import random

day1 = random.randint(1, 28)
day2 = random.randint(1, 31)
hour1 = random.randint(1, 23)
hour2 = random.randint(1, 23)

date1 = datetime.datetime(2024, 2, day1, hour1, 0, 0)
date2 = datetime.datetime(2024, 3, day2, hour2, 0, 0)

difference = date2 - date1
s = difference.total_seconds()
print(s)
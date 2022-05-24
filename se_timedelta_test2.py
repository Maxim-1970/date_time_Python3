from datetime import date as dt
from datetime import timedelta
import sys

tmp = sys.argv[1]
tmp1 = tmp.split('-')
numbers_day = int(sys.argv[2])
# print(tmp1)

start_day = dt(int(tmp1[0]), int(tmp1[1]), int(tmp1[2]))
i = 0
mass = ''
for i in range(numbers_day):
    # print(start_day.strftime("%d.%m.%y"))
    mass += (str(start_day.strftime("%d.%m.%y")))
    if i != numbers_day - 1:
        mass += ', '
    start_day += timedelta(days=7)

print(mass)
# hours=12)
# stop_day = start_day + timedelta(days=14)
# stop_day = start_day - timedelta(days=14)
# stop_day = start_day + days
# print(stop_day)
#
# td = stop_day - start_day
# print(td > day)
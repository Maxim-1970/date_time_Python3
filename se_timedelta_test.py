from datetime import datetime as dt
from datetime import timedelta
import sys

tmp = sys.argv[1]
# print(tmp)

start_day = dt(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]) )
stop_day = dt(int(sys.argv[1]) + 1, 1, 1)
print((stop_day - start_day).days - 1)
# day = timedelta(hours=24)
# days = day * 14 + timedelta(hours=12)
# stop_day = start_day + timedelta(days=14)
# stop_day = start_day - timedelta(days=14)
# stop_day = start_day + days
# print(stop_day)
#
# td = stop_day - start_day
# print(td > day)
from datetime import datetime as dt
from datetime import timedelta

start_day = dt(2016, 1, 19)
day = timedelta(hours=24)
days = day * 14 + timedelta(hours=12)
# stop_day = start_day + timedelta(days=14)
# stop_day = start_day - timedelta(days=14)
stop_day = start_day + days
print(stop_day)

td = stop_day - start_day
print(td > day)
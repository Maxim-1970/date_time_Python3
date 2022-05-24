from datetime import datetime as dt
from dateutil import rrule

start_date = dt(2016, 1, 31)
end_date = dt(2017, 1, 1)

# for date in rrule.rrule(freq=rrule.HOURLY, dtstart=start_date, count=12):
#     print(date)

for date in rrule.rrule(freq=rrule.MONTHLY, dtstart=start_date, until=end_date):
    print(date)
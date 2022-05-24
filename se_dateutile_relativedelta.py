from datetime import datetime as dt
from datetime import timedelta
from dateutil import relativedelta


start_day = dt(2016, 1, 31)
print(start_day + relativedelta.relativedelta(months=1))

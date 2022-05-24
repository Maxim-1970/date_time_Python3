from datetime import datetime as dt
from dateutil import relativedelta
import sys
# python se_dateutile_relativedelta_task.py "2020-04-07" 3
t_date_str = sys.argv[1]
t_date = dt.strptime(t_date_str, "%Y-%m-%d")
print(sys.argv[2])

start_day = t_date
print((start_day + relativedelta.relativedelta(months=1)))

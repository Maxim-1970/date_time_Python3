from datetime import datetime as dt

# now = dt.now()
# print(now)

# p_date = dt(2016,7,29)
# print(p_date.day, p_date.month, p_date.year, sep=".")

# now_str = now.strftime("Текущее время: %d.%m.%Y %H:%M")
# print(now_str)
#
# t_date_str = "1991-05-17"
# t_date = dt.strptime(t_date_str, "%Y-%m-%d")
# print(t_date.strftime("%d %B %Y"))

# p_date = '20190418133454'
import sys

p_date = str(sys.argv[1])
# print(p_date)
md = p_date
i = 0
t_year = md[2] + md[3]
t_month = md[4] + md[5]
t_day = md[6] + md[7]
t_hour = md[8] + md[9]
t_minute = md[10] + md[11]

t_date_str = t_day + '.' + t_month + '.' + t_year + ' ' + t_hour + ':' + t_minute
# t_date = dt.strptime(t_date_str, "%d-%m-%y")
print(t_date_str)



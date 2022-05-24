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
final = ''

p_date_sp = p_date.split(' ')
p_date_sp[1] = p_date_sp[1][:-1]

if p_date_sp[0] == 'January':
    p_date_sp[0] = 'января'
elif p_date_sp[0] == 'February':
    p_date_sp[0] = 'февраля'
elif p_date_sp[0] == 'March':
    p_date_sp[0] = 'марта'
elif p_date_sp[0] == 'April':
    p_date_sp[0] = 'апреля'
elif p_date_sp[0] == 'May':
    p_date_sp[0] = 'мая'
elif p_date_sp[0] == 'June':
    p_date_sp[0] = 'июня'
elif p_date_sp[0] == 'July':
    p_date_sp[0] = 'июля'
elif p_date_sp[0] == 'August':
    p_date_sp[0] = 'августа'
elif p_date_sp[0] == 'September':
    p_date_sp[0] = 'сентября'
elif p_date_sp[0] == 'October':
    p_date_sp[0] = 'октября'
elif p_date_sp[0] == 'November':
    p_date_sp[0] = 'ноября'
elif p_date_sp[0] == 'December':
    p_date_sp[0] = 'декабря'



final = p_date_sp[1] + ' ' + p_date_sp[0] + ' ' + p_date_sp[2]
print( final )






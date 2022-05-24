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
import datetime

p_date = str(sys.argv[1])
final = ''

p_date_sp = p_date.split('-')
# print(p_date_sp)
weekly = datetime.date(int(p_date_sp[0]), int(p_date_sp[1]), int(p_date_sp[2]))
# weekly = datetime.date(int(p_date_sp[0]), int(p_date_sp[1]), int(p_date_sp[2])).isocalendar()[1] - 1

myDateTime =weekly
new_date = weekly
yr = myDateTime.year
weekNumber = int(((myDateTime - datetime.date(yr, 1, 1)).days / 7))

# print(weekNumber)

today = datetime.datetime(int(p_date_sp[0]), int(p_date_sp[1]), int(p_date_sp[2]))
weekly_day = int(f"{today:%j}")
weekNumber = int(f"{today:%W}")
# print(weekly_day)

print('День: ' + str(weekly_day) + ', ' + 'неделя: ' + str(weekNumber))
# print(f'День: {new_date.strftime("%-j")}, неделя: {new_date.strftime("%-W")}')




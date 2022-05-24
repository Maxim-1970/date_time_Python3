from datetime import datetime as dt
import sys

# now = dt.now()
# day = now.strftime("%d.%m.%Y")
# time = now.strftime("%H:%M")
# text = "Начало обучения {day} в {time}".format(day=day, time=time)

# text = "Начало обучения {day:%d.%m.%Y} в {day:%H:%M}".format(day=now)

# text = f"Начало обучения {now:%d.%m.%Y} в {now:%H:%M}"
# print(text)

input = sys.argv[1]
# print(input)
current_dt = input.split(' ')
pref = current_dt[len(current_dt) - 1]
# print(pref)
if pref == 'am':
    print('0' + current_dt[len(current_dt) - 2])
else:
    current_time = current_dt[len(current_dt) - 2].split(':')
    print(str( int(current_time[0]) + 12 ) + ':' + current_time[1] )

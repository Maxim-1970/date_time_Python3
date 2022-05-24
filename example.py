# import datetime
#
# p_date = datetime.date(2001, 9, 13)
# print(p_date.day, p_date.month, p_date.year, sep='.')
# print(p_date.isoweekday())
# print(p_date.replace(year=2016, day=12))
# print(p_date)
# print(datetime.date.today())

import sys
import datetime

if len(sys.argv) == 4:
    p_date = datetime.date(int(sys.argv[1]),
                           int(sys.argv[2]),
                           int(sys.argv[3]))
    print(p_date.isoweekday())
    weekly_day = p_date.isoweekday()
    if weekly_day == 1:
        print('понедельник')
    if weekly_day == 2:
        print('вторник')
    if weekly_day == 3:
        print('среда')
    if weekly_day == 4:
        print('четверг')
    if weekly_day == 5:
        print('пятница')
    if weekly_day == 6:
        print('суббота')
    if weekly_day == 7:
        print('воскресенье')

else:
    print('не то что-то с агрументами.')
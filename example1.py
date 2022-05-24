import sys
import datetime

if len(sys.argv) == 4:
    p_date = datetime.date(int(sys.argv[1]),
                           int(sys.argv[2]),
                           int(sys.argv[3]))
    p_date_today = datetime.date.today()

    if p_date > p_date_today:
        print('Будущее')
    elif p_date < p_date_today:
        print('Прошлое')
    elif p_date == p_date_today:
        print('Настоящее')

    # print(p_date.isoweekday())
    # weekly_day = p_date.isoweekday()
    # if weekly_day == 1:
    #     print('понедельник')
    # if weekly_day == 2:
    #     print('вторник')
    # if weekly_day == 3:
    #     print('среда')
    # if weekly_day == 4:
    #     print('четверг')
    # if weekly_day == 5:
    #     print('пятница')
    # if weekly_day == 6:
    #     print('суббота')
    # if weekly_day == 7:
    #     print('воскресенье')

else:
    print('не то что-то с агрументами')
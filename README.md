# date_time_Python3
Отработка курса Шультайс образование
Дата время в Python
ВВЕДЕНИЕ В DATETIME
Для работы с датой и временем служит модуль datetime он включает следующие классы:
- date
- time
- datetime
- timedelta
а также два класса для работы с часовыми поясами
- tzinfo
- timezone
#работа класса date(инициализация)
import datetime
p_date = datetime.date(2015, 9, 13) #год месяц число
print(p_date)   #получим дату в международном формате
print(p_date, p_date.month, p_date.year, sep=".")
#ручное преобразование даты в строку
var = str(p_date.day) +'.'+ str(p_date.month) +'.'+ str(p_date.year)
print(var)
#выражение возвращает день недели начиная 
print(p_date.isoweekday())  #с 1(понедельник)
print(p_date.weekday())     #с 0(понедельник)
#если надо изменить дату то используем
p_date = p_date.replace(year=2016, day=12)
print(p_date)
#на выходе получаем 
2016-09-12
#создание сегоднешней даты
print(datetime.date.today())
---------------------------------------------
КЛАСС TIME
#инициализация объекта
from datetime import time
t = time(14, 45, 36)
print(t)
# как и дату время можно разбить на отдельные int
print(t.hour, t.minute, t.second, t.microsecond)
#также действует метод replace
print(t.replace(hour=15))
---------------------------------------------
КЛАСС DATETIME
from datetime import datetime as dt
now = dt.now()  #формируется объект с текущем временем и датой
print(now.day, now.month, now.year, now.hour, now.minute) 
---------------------------------------------
ФОРМАТИРОВАНИЕ
#Перевод объекта дата в строку (метод strftime)
from datetime import datetime as dt
now = dt.now()
now_str = now.strftime("%d.%m.%Y") #метод strftime принимает строку форматирования
#Перевод строки со временем в объект дата (метод strptime)
t_date_str = "1991-05-17"
t_date = dt.strptime(t_date_str, "%Y-%m-%d")
----------------------------------------------
ФОРМАТИРОВАНИЕ, ЧАСТЬ 2
from datetime import datetime as dt

now = dt.now()
day = now.strftime("%d.%m.%Y")
time = now.strftime("%H:%M")
#три варианта вывести объект datetime в строку
text1 = "Начало обучения {day} в {time}".format(day=day, time=time)
text2 = "Начало обучения {day:%d.%m.%Y} в {day:%H:%M}".format(day=now)
text3 = f"Начало обучения {now:%d.%m.%Y} в {now:%H:%M}"

print(text1)
print(text2)
print(text3)
-----------------------------------------------
TIMEDELTA
from datetime import datetime as dt
from datetime import timedelta

start_day = dt(2016, 1, 19)
stop_day = start_day + timedelta(days=14)#возможные значение
                                        #seconds,
                                        #minutes
                                        #hours
                                        #weeks
print(stop_day)
#объект timedelta может быть получен путем вычитания одной даты
#из другой
-----------------------------------------------
МОДУЛЬ DATEUTIL
Модуль DATEUTIL не входит в комплект поставки python его надо устанавливать
отдельно по команде
pip install python-dateutil
#использоване модуля dateutil для распознавание даты
from dateutil.parser import parse

dates = [
    "2016/07/11 13:35",
    "07/11/16 13:35",
    "2016-07-11 13:35:00",
    "11 jul 2016, 13:35"
]

for date in dates:
    print(parse(date))
#использование модуля dateutil для создания временных интервалов
from datetime import datetime as dt
from dateutil import relativedelta
start_day = dt(2016, 1, 31)
print(start_day + relativedelta.relativedelta(months=1))
#использования модуля для формирование последовательности времени 
#по заданным условиям
from datetime import datetime as dt
from dateutil import relativedelta
from dateutil import rrule
start_date = dt(2016, 1, 31)
for date in rrule.rrule(freq=rrule.HOURLY, dtstart=start_date, count=12):
    print(date)
#пример 2. Формирование промежутков между датами
from datetime import datetime as dt
from dateutil import relativedelta
from dateutil import rrule
start_date = dt(2016, 1, 31)
end_date = dt(2017, 1, 1)
for date in rrule.rrule(freq=rrule.MONTHLY, dtstart=start_date, until=end_date):
    print(date)    


----------------------------------------------
----------------------------------------------
---------------------------------------------- 
1. Перевод даты времени из одного формата в другой средствами python
Используется когда формат даты известен
from datetime import datetime as dt             #импорт модуля
t_date_str = "1991-05-17"                       #строка с датой которую надо перевести из формата в формат 
t_date = dt.strptime(t_date_str, "%Y-%m-%d")    #перегоняем строку в объект datetime
print(t_date.strftime("%d %B %Y"))              #перегоняем объект datetime обратно в строку с нужным форматом
2. Можно перегонять дату из строки в объект при помощи модуля dateutil (pip install python-dateutil)
Используется когда формат даты не известен
from dateutil.parser import parse

dates = [
    "2016/07/11 13:35",
    "07/11/16 13:35",
    "2016-07-11 13:35:00",
    "11 jul 2016, 13:35"
]

for date in dates:
    print(parse(date))  #использование модуля
    
3.1. Организация временного смещения на 7 дней и менее
from datetime import datetime as dt
from datetime import timedelta

start_day = dt(2016, 1, 31)         #исходная дата
print(start_day + timedelta(days=7))#смещение даты

3.2. Смещение на календарный месяц(по такому принципу работают банки)
from datetime import datetime as dt
from dateutil import relativedelta

start_day = dt(2016, 1, 31)                              #исходная дата
print(start_day + relativedelta.relativedelta(months=1)) #29 февраля

4. Генерация даты по заданной последовательности
from datetime import datetime as dt
from dateutil import rrule

start_date = dt(2016, 1, 31)
end_date = dt(2017, 1, 1)
#генерация 12 объектов с интервалом 1 час
for date in rrule.rrule(freq=rrule.HOURLY, dtstart=start_date, count=12):
    print(date)



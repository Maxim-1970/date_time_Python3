from datetime import datetime as dt

now = dt.now()
# day = now.strftime("%d.%m.%Y")
# time = now.strftime("%H:%M")
# text = "Начало обучения {day} в {time}".format(day=day, time=time)

# text = "Начало обучения {day:%d.%m.%Y} в {day:%H:%M}".format(day=now)

text = f"Начало обучения {now:%d.%m.%Y} в {now:%H:%M}"
print(text)


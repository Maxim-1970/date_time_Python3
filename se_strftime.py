from datetime import datetime as dt

now = dt.now()
print(now)

# p_date = dt(2016,7,29)
# print(p_date.day, p_date.month, p_date.year, sep=".")

now_str = now.strftime("Текущее время: %d.%m.%Y %H:%M")
print(now_str)

t_date_str = "1991-05-17"
t_date = dt.strptime(t_date_str, "%Y-%m-%d")
print(t_date.strftime("%d %B %Y"))
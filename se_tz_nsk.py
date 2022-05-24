from datetime import datetime as dt
from pytz import timezone

nsk_tz = timezone("Asia/Novosibirsk")

doc = open("post.txt")
date, content = doc.readlines()
date = dt.strptime(date.strip(), '%Y-%m-%d %H:%M:%S %Z%z')
print(date)
date = date.astimezone(nsk)
print(date)

doc.close()
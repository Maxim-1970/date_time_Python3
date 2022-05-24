from datetime import datetime as dt

formats = [
    "%Y/%m/%d %H:%M",
    "%m/%d/%y %H:%M",
    "%Y-%m-%d %H:%M:%S",
    "%d %d %Y, %H:%M",
    "%d.%m.%Y %H:%M"
]

dates = [
    "2016/07/11 13:35",
    "07/11/16 13:35",
    "2016-07-11 13:35:00",
    "11 jul 2016, 13:35",
    "11 07 2016 13:35"
]

for date_str in dates:
    for date_format in formats:
        try:
            date = dt.strptime(date_str, date_format)
            print(date)
        except:
            continue
from dateutil.parser import parse

dates = [
    "2016/07/11 13:35",
    "07/11/16 13:35",
    "2016-07-11 13:35:00",
    "11 jul 2016, 13:35"
]

for date in dates:
    print(parse(date))
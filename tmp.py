from datetime import datetime as dt
from pytils import dt as ru_dt

date = dt(1970, 4 , 16)
print(ru_dt.ru_strftime("%d %B %Y %A", date, inflected=True,
                        inflected_day=True, preposition=True))
end_date = dt.now()

# print(ru_dt.distance_fo_time_in_words(date, to_time=end_date))
print(ru_dt.distance_of_time_in_words(date, to_time=end_date))

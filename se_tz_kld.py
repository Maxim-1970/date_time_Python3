from datetime import datetime as dt
import pytz

kld_tz = pytz.timezone("Europe/Kaliningrad")

post = "{}\n{}".format(
    dt.now(tz=kld_tz).strftime('%Y-%m-%d %H:%M:%S %Z%z'),
    "Very important document"
)

doc = open("post.txt", "w+")
doc.write(post)
doc.close()
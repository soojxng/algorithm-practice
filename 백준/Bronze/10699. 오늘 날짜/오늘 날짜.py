import datetime

kst = datetime.timezone(datetime.timedelta(hours=9))
print(str(datetime.datetime.now(kst))[:10])
import datetime
now = datetime.datetime.now()
d=now.date()
t=now.time()
print(datetime.datetime.combine(d, t))

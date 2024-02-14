import datetime

a = datetime.datetime.now()
delta = datetime.timedelta(days=5)
a -= delta
print(a)
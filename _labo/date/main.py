import datetime

print(datetime.datetime.today().isoformat())

d = datetime.datetime.today()

print("%s:%s:%s:%s:%s" % (d.year, d.month, d.day, d.hour, d.minute))

print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)

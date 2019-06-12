import datetime

start = datetime.date(1901, 1, 1)
sundays = 0
while start != datetime.date(2000, 12,31):
    if start.weekday() == 6 and start.day == 1:
        sundays += 1
    start += datetime.timedelta(days=1)

print(sundays)
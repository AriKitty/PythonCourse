import datetime
import pytz

# w/o timezone information
localTime = datetime.datetime.now()
utcTime = datetime.datetime.utcnow()
print("Naive local time {}".format(localTime))
print("Naive UTC {}".format(utcTime))

# With timezone information
awareLocalTime = pytz.utc.localize(utcTime).astimezone()
awareUtcTime = pytz.utc.localize(utcTime)
print("Aware local time {}, time zone {}".format(awareLocalTime, awareLocalTime.tzinfo))
print("Aware UTC {}, time zone {}".format(awareUtcTime, awareUtcTime.tzinfo))


gapTime = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gapTime)
print(gapTime.timestamp())

s = 1445733000
t = s + (60 * 60)

gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(t, dt2))

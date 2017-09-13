from datetime import datetime
import pytz

# Comparing#  dates
a = datetime(2016, 4, 13)
b = datetime(2016, 3, 13)

print(a < b)

# Careful when comparing automatic dates
print('\n')
c = datetime.now()
d = datetime.now()
if c == d:
    print('???Equal???')
else:
    print('Not equal, because of microseconds')

# Math operations - only supports substractions
print(a - b)

# Timezones
zone_sofia = pytz.timezone('Europe/Sofia')
print(datetime.now(tz=zone_sofia))
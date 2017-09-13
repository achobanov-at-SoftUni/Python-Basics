import datetime

a = datetime.datetime(100, 1, 1, 11, 34, 59)
b = a + datetime.timedelta(hours = 3)

print(a)
print(b)
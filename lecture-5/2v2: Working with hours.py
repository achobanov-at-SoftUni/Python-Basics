from datetime import datetime, timedelta

FILEPATH = '/home/alex/Documents/SoftUni/open_courses/python/lecture-5/sales.csv'
hours = {
    '00:00:00': 0,
    '01:00:00': 0,
    '02:00:00': 0,
    '03:00:00': 0,
    '04:00:00': 0,
    '05:00:00': 0,
    '06:00:00': 0,
    '07:00:00': 0,
    '08:00:00': 0,
    '09:00:00': 0,
    '10:00:00': 0,
    '11:00:00': 0,
    '12:00:00': 0,
    '13:00:00': 0,
    '14:00:00': 0,
    '15:00:00': 0,
    '16:00:00': 0,
    '17:00:00': 0,
    '18:00:00': 0,
    '19:00:00': 0,
    '20:00:00': 0,
    '21:00:00': 0,
    '22:00:00': 0,
    '23:00:00': 0
}
with open(FILEPATH) as sales_file:
    for line in sales_file:
        data = line.split(',')
        time = data[0].split()
        time_value = datetime.strptime(time[1], '%H:%M:%S').time().replace(minute = 0, second = 0)
        hours[str(time_value)] += round(float(data[1]), 2)

keys_list = list(hours.keys())
values_list = list(hours.values())
print('{}: {}'.format(
    keys_list[values_list.index(max(values_list))],
    max(values_list)
))
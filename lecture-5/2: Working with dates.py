FILEPATH = '/home/alex/Documents/SoftUni/open_courses/python/lecture-5/sales.csv'

days = ['2015-11-23', '2015-11-24', '2015-11-25', '2015-11-26']
sums = [0, 0, 0, 0]
errors = []
line_num = 0
with open(FILEPATH) as sales_file:
    for line in sales_file:
        line_num += 1
        data = line.split(',')
        for day in range(0, 4):
            if days[day] in data[0]:
                try:
                    sums[day] += float(data[1])
                except:
                    errors.append(line_num)
                    continue

# ???????????????????
# for sum in sums:
#     sum = round(sum, 2)

for sum in range(4):
    sums[sum] = (round(sums[sum], 2))

print('Date: {}: {}'.format(
    days[sums.index(max(sums))],
    max(sums)
))
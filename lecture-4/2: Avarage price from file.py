catalog = input('full or sample catalog? ')
if catalog == 'full':
    address = '/home/alex/Documents/SoftUni/open_courses/python/lecture-4/catalog_full.csv'
else:
    address = '/home/alex/Documents/SoftUni/open_courses/python/lecture-4/catalog_sample.csv'


def get_info(product: str):
    list = product.split(',')
    value = float(list[6])
    return value


highest = 0
highest_dup = 1
lowest = 0
lowest_dup = 1
sum = 0
counter = 0
line_num = 1
with open(address) as f:
    for line in f:
        price = get_info(line)
        # Removing the minimal and maximal values ( because why not )
        if highest == 0 or lowest == 0:
            highest = price
            lowest = price
        elif price > highest:
            highest = price
            highest_dup = 1
        elif price < lowest:
            lowest = price
            lowest_dup = 1
        elif price == highest:
            highest_dup += 1
        elif price == lowest:
            lowest_dup += 1

        sum += price
        counter += 1

print('{0:.2f}'.format((sum - highest_dup * highest - lowest_dup * lowest) / counter))



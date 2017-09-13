# Commented text is an implemented solution to remove the highest and lowest values, if necessary
import logging

catalog = input('full or sample catalog? ')
if catalog == 'full':
    address = '/home/alex/Documents/SoftUni/open_courses/python/lecture-4/catalog_full.csv'
else:
    address = '/home/alex/Documents/SoftUni/open_courses/python/lecture-4/catalog_sample.csv'


def get_info(product: str, data: str):
    holder = product.split(',')
    try:
        if data == 'price':
            return float(holder[6])
        else:
            return holder[5]
    except:
        return 'exception'

line_issue = []
for target in range(5):
    #
    # highest = 0
    # highest_dup = 1
    # lowest = 0
    # lowest_dup = 1
    sum = 0
    counter = 0
    targets = ['Men', 'Woman', 'Unisex', 'Kid', 'Infant']
    line_num = 0
    with open(address) as catalog:
        for line in catalog:
            line_num += 1
            info = get_info(line, 'target')
            price = get_info(line, 'price')
            # data issues check
            if info not in targets or (price or info) == 'exception':
                if line_num not in line_issue:
                    line_issue.append(line_num)
                continue
            if info == targets[target]:
                #
                # if highest == 0 or lowest == 0:
                #     highest = price
                #     lowest = price
                # elif price > highest:
                #     highest = price
                #     highest_dup = 1
                # elif price < lowest:
                #     lowest = price
                #     lowest_dup = 1
                # elif price == highest:
                #     highest_dup += 1
                # elif price == lowest:
                #     lowest_dup += 1

                sum += price
                counter += 1

    print('{0:.2f}'.format(sum / counter))
    #
    # print('{0:.2f}'.format((sum - highest_dup * highest - lowest_dup * lowest) / counter))
if len(line_issue) > 0:
    logging.warning(' Incorrect data on lines: {}'.format(line_issue))
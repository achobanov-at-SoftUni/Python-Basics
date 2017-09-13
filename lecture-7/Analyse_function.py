# Не-пълна имплементация на същата програма, но без обекти. По този начин написана се изпълнява приблизително
# 3 пъти по-бързо, зщото има само един цикъл, спрямо 5те, които се изпълняват при обектите.
import csv
import logging
import pytz

from datetime import datetime

CATALOG_PATH = '/home/alex/Documents/SoftUni/open_courses/python/lecture-7/Analyse_object/catalog.csv'
SALES_PATH = '/home/alex/Documents/SoftUni/open_courses/python/lecture-7/Analyse_object/sales-1M.csv'


def load_data(input_file):
    with open(input_file) as f:
        holder = csv.reader(f)
        file_data = list(holder)
    return file_data

import iso8601

sales_data = load_data(SALES_PATH)
catalog_data = load_data(CATALOG_PATH)

sales = 0  # Summary
sales_sum = 0
date_start = datetime(2016, 1, 1, 00, 00, 0, 0, pytz.utc)
date_end = date_start

top_categories_tmp = {}  # Top Five
top_cities = {}
top_hours = {}

for row in sales_data:

    # Summary
    sales += 1
    try:
        cost = float(row[4])
        date = iso8601.parse_date(row[3])
    except:
        logging.warning('data issue on line: {}'.format(sales))

    sales_sum += cost
    if date < date_start:
        date_start = date
    elif date > date_end:
        date_end = date

    # Top Five
    hour = iso8601.parse_date(row[3])
    hour = hour.replace(minute=0, second=0, microsecond=0)
    QUERIES = {
        'category': row[0],
        'city': row[2],
        'hour': hour.astimezone(pytz.utc)
    }
    if QUERIES['category'] in top_categories_tmp:
        top_categories_tmp[QUERIES['category']] += float(row[4])
        top_categories_tmp[QUERIES['category']] = round(top_categories_tmp[QUERIES['category']], 2)
    else:
        top_categories_tmp[QUERIES['category']] = float(row[4])

    if QUERIES['city'] in top_cities:
        top_cities[QUERIES['city']] += float(row[4])
        top_cities[QUERIES['city']] = round(top_cities[QUERIES['city']], 2)
    else:
        top_cities[QUERIES['city']] = float(row[4])

    if QUERIES['hour'] in top_hours:
        top_hours[QUERIES['hour']] += float(row[4])
        top_hours[QUERIES['hour']] = round(top_hours[QUERIES['hour']], 2)
    else:
        top_hours[QUERIES['hour']] = float(row[4])

top_categories = {}
list_top_five_keys = sorted(top_categories_tmp, key=top_categories_tmp.get, reverse=True)[:5]  # Getting top 5 categories.
for key in list_top_five_keys:
    for row in catalog_data:
        if key == row[0]:
            key_string = row[5] + ', ' + row[4]
            top_categories[key_string] = top_categories_tmp[key]

sales_avrg = round(sales_sum, 2) / sales

print(
    """
Обобщение
---------
    Общ брой продажби: {}
    Обща сума продажби: {}
    Средна цена на продажба: {}
    Начало на период на данни: {}
    Край на период на данни: {}
    """.format(sales, sales_sum, sales_avrg, date_start, date_end)
)

# for var in range(3):
#     DATA = {
#         # '0': top_categories,
#         '1': top_cities,
#         '2': top_hours
#     }
# print(
#     """
# Най-много продажби по категории, градове, часове (top 5)
# ------------------------------------------------
#     {} : {} $
#     {} : {} $
#     {} : {} $
#     {} : {} $
#     {} : {} $
#     """.format(
#             top_categories[0], sales_data[top_categories[0]],
#             top_categories[1], sales_data[top_categories[1]],
#             top_categories[2], sales_data[top_categories[2]],
#             top_categories[3], sales_data[top_categories[3]],
#             top_categories[4], sales_data[top_categories[4]]
#         )
# )
print(
    """
Най-много продажби по категории, градове, часове (top 5)
------------------------------------------------
    {} : {} $
    {} : {} $
    {} : {} $
    {} : {} $
    {} : {} $
    """.format(
            top_cities[0], sales_data[top_cities[0]],
            top_cities[1], sales_data[top_cities[1]],
            top_cities[2], sales_data[top_cities[2]],
            top_cities[3], sales_data[top_cities[3]],
            top_cities[4], sales_data[top_cities[4]]
        )
)
print(
    """
Най-много продажби по категории, градове, часове (top 5)
------------------------------------------------
    {} : {} $
    {} : {} $
    {} : {} $
    {} : {} $
    {} : {} $
    """.format(
            top_hours[0], sales_data[top_hours[0]],
            top_hours[1], sales_data[top_hours[1]],
            top_hours[2], sales_data[top_hours[2]],
            top_hours[3], sales_data[top_hours[3]],
            top_hours[4], sales_data[top_hours[4]]
        )
)

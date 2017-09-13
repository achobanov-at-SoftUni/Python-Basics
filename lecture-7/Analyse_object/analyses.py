import iso8601
import logging
import pytz

from datetime import datetime


class Summary:

    def __init__(self, sales_data):
        self.sales_data = sales_data

    def analyse(self):
        DATA = self.sales_data

        sales = 0
        sales_sum = 0
        date_start = datetime(2016, 1, 1, 00, 00, 0, 0, pytz.utc)
        date_end = date_start

        for row in DATA:
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
        sales_avrg = round(sales_sum, 2) / sales

        return sales, round(sales_sum, 2), sales_avrg, date_start, date_end


class TopFive:

    def __init__(self, catalog_data, sales_data, query):
        self.catalog_data = catalog_data
        self.sales_data = sales_data
        self.query = query

    def analyse(self):
        CATALOG_DATA = self.catalog_data
        SALES_DATA = self.sales_data
        query = self.query

        products = {}
        # Creating a dict with ID, city or hour ( depending on query ) as keys and their income as values.
        for row in SALES_DATA:
            hour = iso8601.parse_date(row[3])
            hour = hour.replace(minute=0, second=0, microsecond=0)
            QUERIES = {
                'category': row[0],
                'city': row[2],
                'hour': hour.astimezone(pytz.utc)
            }
            if QUERIES[query] in products:
                products[QUERIES[query]] += float(row[4])
                products[QUERIES[query]] = round(products[QUERIES[query]], 2)
            else:
                products[QUERIES[query]] = float(row[4])

        if query == 'category':
            top_five = {}
            top_five_items = sorted(products, key=products.get, reverse=True)[:5]  # Getting top 5 categories.
            for key in top_five_items:
                for row in CATALOG_DATA:
                    if key == row[0]:
                        key_string = row[5] + ', ' + row[4]
                        top_five[key_string] = products[key]

            return top_five
        else:
            return products



import sys

from loaders import LoaderCSV
from output import PrintSummary, PrintTopFive

from Analyse_object.analyses import Summary, TopFive

CATALOG_PATH = '/home/alex/Documents/SoftUni/open_courses/python/lecture-7/Analyse_object/catalog.csv'
SALES_PATH = '/home/alex/Documents/SoftUni/open_courses/python/lecture-7/Analyse_object/sales-1M.csv'


def main():
    catalog_data = load_data(CATALOG_PATH)
    sales_data = load_data(SALES_PATH)
    output_data = analyse(catalog_data, sales_data)
    print_data(output_data)


def load_data(input_file):
    holder = LoaderCSV(input_file)
    data = holder.load()
    return data


def analyse(catalog_data, sales_data):
    holder = Summary(sales_data=sales_data)
    summary_data = holder.analyse()

    holder = TopFive(catalog_data=catalog_data, sales_data=sales_data, query='category')
    top_category = holder.analyse()

    holder = TopFive(catalog_data=catalog_data, sales_data=sales_data, query='city')
    top_city = holder.analyse()

    holder = TopFive(catalog_data=catalog_data, sales_data=sales_data, query='hour')
    top_hour = holder.analyse()

    return summary_data, top_category, top_city, top_hour


def print_data(output_data):
    holder = PrintSummary(output_data[0])
    holder.print()

    holder = PrintTopFive(output_data[1], query='category')
    holder.print()

    holder = PrintTopFive(output_data[2], query='city')
    holder.print()

    holder = PrintTopFive(output_data[3], query='hour')
    holder.print()

if __name__ == "__main__":
    sys.exit(main())

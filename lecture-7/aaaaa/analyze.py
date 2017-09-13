import sys
import os
from analysis_functions import (
    print_summary,
    print_sales_amount_by_city,
)
from sales import load_sales_data
from catalog import load_catalog_by_item_id

DISPLAY_TOP = 5


def main():
    try:
        # parse command line arguments
        filename_catalog, filename_sales = _parse_command_line_parameters()
        print(filename_catalog, filename_sales)

        # load sales data
        sales = load_sales_data(filename_sales)
        catalog_by_item_id = load_catalog_by_item_id(filename_catalog)

        # calculate and print summaries
        print_summary(sales)
        print_sales_amount_by_city(sales)

        return 0
    except Exception as e:
        print("Error: " + str(e))
        raise
        # return 1


def _parse_command_line_parameters():
    if len(sys.argv) < 3:
        raise ValueError("Usage: {}  <catalog.csv> <sales.csv>".format(sys.argv[0]))

    filename_catalog, filename_sales = sys.argv[1:3]
    if not os.path.isfile(filename_catalog)\
            or not os.access(filename_catalog, os.R_OK):
        raise ValueError("Invalid or inaccessible catalog file: '{}'".format(filename_catalog))

    if not os.path.isfile(filename_sales)\
            or not os.access(filename_sales, os.R_OK):
        raise ValueError("Invalid or inaccessible catalog file: '{}'".format(filename_sales))

    return filename_catalog, filename_sales



if __name__ == "__main__":
    sys.exit(main())

import csv
import logging


class LoaderCSV:

    def __init__(self, file):
        self.file = file

        if file is None:
            logging.warning('Missing input file.')

    def load(self):
        with open(self.file) as f:
            holder = csv.reader(f)
            file_data = list(holder)
        return file_data


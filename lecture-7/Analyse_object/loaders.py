
import csv
import os


class LoaderCSV:

    def __init__(self, file):
        self.file = file

        if os.path.exists(file) is False:
            # logging.warning('Missing input file.')
            self.file = input('File not found! Enter location: ')

    def load(self):
        with open(self.file) as f:
            holder = csv.reader(f)
            file_data = list(holder)
        return file_data


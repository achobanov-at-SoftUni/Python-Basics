import csv


class CatalogEntry:

    def __init__(self, item_id, category_name):
        self.item_id = str(item_id)
        self.category_name = str(category_name)

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, str(self.__dict__))


def load_catalog_by_item_id(filename_catalog):
    with open(filename_catalog) as f:
        catalog = {}   # item_id: CategoryEntry
        for catalog_row in csv.reader(f):
            # TODO: check if the row is correct
            catalog[catalog_row[0]] = CatalogEntry(
                item_id=catalog_row[0],
                category_name=catalog_row[5],
            )
        return catalog


if __name__ == "__main__":
    pass
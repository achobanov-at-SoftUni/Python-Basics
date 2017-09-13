import json
import yaml


class Loader:

    def __init__(self, filename):
        self.filename = filename

    def load(self):
        pass


class JSONLoader(Loader):

    def load(self):
        with open(self.filename) as to_draw_json:
            input_data = json.load(to_draw_json)
            return input_data


class YAMLLoader(Loader):

    def load(self):
        with open(self.filename) as to_draw_yaml:
            input_data = yaml.load(to_draw_yaml)
            return input_data

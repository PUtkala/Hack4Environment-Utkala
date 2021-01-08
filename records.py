import numpy as np

class Record():
    def __init__(self, index, properties):
        self.index = index
        self.datetime = properties.datetime
        self.filename = properties.filename
        self.lat = properties.lat
        self.lon = properties.lon
        self.model = properties.model
        self.photo_id = properties.photo_id
        self.result_string = properties.result_string

    def load_dataset():
        pass


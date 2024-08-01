import csv
import pkgutil


class Reciter:
    def __init__(self):
        self.reciters_data = self.load_reciters_data()

    def load_reciters_data(self):
        data = pkgutil.get_data(__name__, 'reciters.csv')
        reciters = {}
        if data:
            lines = data.decode().splitlines()
            reader = csv.DictReader(lines)
            for row in reader:
                reciters[row['ID']] = row['Full Name']
        return reciters

    def show_reciters(self):
        return self.reciters_data

    def get_reciter_name(self, reciter_id):
        return self.reciters_data.get(reciter_id, )

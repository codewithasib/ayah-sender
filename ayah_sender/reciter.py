import csv
import pkgutil


class Reciter:
    def __init__(self):
        """
        Constructor
        """
        self.file_path = 'reciters.csv'
        self.reciters_data = self._read_reciters_data()

    def _read_reciters_data(self):
        """
        Reads the reciter data from the csv file.
        :return:
        """
        reciters_data = {}
        with open(self.file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                reciters_data[row['ID']] = row['Full Name']
        return reciters_data

    def show_reciters(self):
        """
        Returns the reciters_data
        :return:
        """
        return self.reciters_data

    def get_reciter_name(self, reciter_id):
        """
        Returns the name of the reciter
        :param reciter_id:
        :return:
        """
        reciter_id = str(reciter_id)
        return self.reciters_data[reciter_id]


if __name__ == '__main__':
    reciter = Reciter()
    name = reciter.get_reciter_name('46')
    print(name)


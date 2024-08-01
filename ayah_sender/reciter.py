import csv, json
from pathlib import Path
from importlib.resources import files


class Reciter:
    def __init__(self):
        """
        Constructor
        """
        self.reciters_data = self._read_reciters_data()

    def _read_reciters_data(self):
        """
        Reads the reciter data from the csv file.
        :return:
        """
        reciters_data = {}
        # Use the newer files API to access reciters.csv
        reciters_csv_path = Path(files('ayah_sender') / 'reciters.csv')
        with reciters_csv_path.open('r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                reciters_data[row['ID']] = row['Full Name']
        return reciters_data

    def show_reciters(self):
        """
        Returns the reciters_data
        :return:
        """
        formatted_reciters_data = json.dumps(self.reciters_data, indent=4)
        return formatted_reciters_data

    def get_reciter_name(self, reciter_id):
        """
        Returns the name of the reciter
        :param reciter_id:
        :return:
        """
        reciter_id = str(reciter_id)
        return self.reciters_data[reciter_id]


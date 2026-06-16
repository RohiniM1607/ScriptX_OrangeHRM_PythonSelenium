import csv

class CSVReader:
    @staticmethod
    def get_data(file_path):

        data = []

        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                data.append(row)

        return data
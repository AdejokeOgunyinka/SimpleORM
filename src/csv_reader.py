import csv


class CsvReader:
    """ This class contains a static method that reads the csv file, whether it's authors.py or books.py."""
    @staticmethod
    def read_csv(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            data = [row for row in reader]

        return data

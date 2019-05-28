import csv
from typing import Generator
from collections import OrderedDict


class CsvConnector:
    """
    Class responsible for opening a connection
    with the csv file.
    """
    def __init__(self, file_path: str):
        self._file_path = file_path

    def connect(self) -> Generator[OrderedDict]:
        """
        Opens the csv file and returns a generator,
        in order to deal with large csv files.
        """
        try:
            with open(self._file_path, 'r') as fh:
                reader = csv.DictReader(fh)
                yield next(reader)
        except FileNotFoundError:
            print('File was not found')

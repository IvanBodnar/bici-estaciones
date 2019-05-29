import csv


class CsvConnector:
    """
    Class responsible for opening a connection
    with the csv file.
    """
    def __init__(self, file_path: str):
        self._file_path = file_path
        self.fh = None

    @property
    def reader(self) -> csv.DictReader:
        """
        Opens the csv file and returns a DictReader.
        """
        try:
            self.fh = open(self._file_path, 'r')
            return csv.DictReader(self.fh)
        except FileNotFoundError:
            print('File was not found')


class CsvFetcher:
    def __init__(self, connector: CsvConnector):
        self._connector = connector

    def fetch_filtered(self):
        reader = self._connector.reader

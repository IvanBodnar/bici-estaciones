import csv
from datetime import time
from datetime import datetime
from collections import Counter, namedtuple


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


class Row:
    def __init__(self, start_station: str):
        self._start_station = start_station

    @property
    def start_station(self):
        return self._start_station.lower().strip()

    def __repr__(self):
        return 'Row ' + str(self._start_station)


class CsvFetcher:
    def __init__(self, connector: CsvConnector, filter_range_start: str, filter_range_end: str):
        self._connector = connector
        self._filter_range_start = self._convert_to_time(filter_range_start)
        self._filter_range_end = self._convert_to_time(filter_range_end)

    @staticmethod
    def _convert_to_time(time_string: str):
        return time.fromisoformat(time_string)

    def _is_in_time_range(self, travel_start_time: str):
        travel_start_time_object = datetime.fromisoformat(travel_start_time).time()
        return self._filter_range_start <= travel_start_time_object <= self._filter_range_end

    def fetch_filtered(self):
        reader = self._connector.reader
        filtered = (Row(row['bici_nombre_estacion_origen']).start_station for row in reader if self._is_in_time_range(row['bici_Fecha_hora_retiro']))
        c = Counter(filtered)
        l = sorted([x for x in c.items()], key=lambda x: x[1], reverse=True)[0:3]
        print(l)

import csv
from datetime import time
from datetime import datetime
from collections import Counter
from typing import List

from bici_estaciones.business.station import Station


class CsvConnector:
    """
    Class responsible for opening a connection
    with the csv file.
    :param file_path: str representing the path to the csv file to be read.
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
        except FileNotFoundError as e:
            raise e


class Row:
    """
    Represents a csv row
    :param start_station: the name of the station from which bikes depart.
    """
    def __init__(self, start_station: str):
        self._start_station = start_station

    @property
    def start_station(self):
        """
        Cleans and returns the station's name
        :return:
        """
        return self._start_station.lower().strip()

    def __repr__(self):
        return 'Row ' + str(self._start_station)


class CsvFetcher:
    """
    Fetches data from the csv file. A time range must be
    passed on instantiation to filter the data.
    :param connector: CsvConnector instance.
    :param filter_range_start: str representing the start time of the time range to use.
    :param filter_range_end: str representing the end time of the time range to use.
    """
    def __init__(self, connector: CsvConnector, filter_range_start: str, filter_range_end: str):
        self._connector = connector
        self._filter_range_start = self._convert_to_time(filter_range_start)
        self._filter_range_end = self._convert_to_time(filter_range_end)

    @staticmethod
    def _convert_to_time(time_string: str):
        """
        Helper method to convert a string representing a datetime
        to a time object.
        :param time_string: date and time string in iso format.
        :return void:
        """
        return time.fromisoformat(time_string)

    def _is_in_time_range(self, travel_start_time: str) -> bool:
        """
        Evaluates if the start time of the bike's travel is
        contained in the required time range.
        :param travel_start_time: iso datetime string representing the date and
        time the travel began.
        """
        travel_start_time_object = datetime.fromisoformat(travel_start_time).time()
        return self._filter_range_start <= travel_start_time_object <= self._filter_range_end

    def fetch_filtered(self, amount: int) -> List[Station]:
        """
        Filters and fetches the required data from the csv, using
        a generator that loads the data using the given time filter.
        Returns a list of namedtuples containing the name of the station
        and the amount of travels started on that station.
        :param amount: int representing the amount of stations to return.
        """
        try:
            reader = self._connector.reader
            filtered_gen = (
                Row(row['bici_nombre_estacion_origen']).start_station
                for row in reader
                if self._is_in_time_range(row['bici_Fecha_hora_retiro'])
            )
            counter = Counter(filtered_gen)
            return sorted(
                [Station(*station) for station in counter.items()],
                key=lambda station: station.departures_amount,
                reverse=True
            )[0:amount]
        finally:
            self._connector.fh.close()

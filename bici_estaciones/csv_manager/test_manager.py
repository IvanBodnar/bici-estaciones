from collections import OrderedDict
from datetime import time

import pytest

from bici_estaciones.csv_manager.manager import CsvConnector, Row, CsvFetcher


class TestCsvConnector:

    def test_creates(self):
        connector = CsvConnector('./bici_estaciones/csv_manager/recorridos.csv')
        assert isinstance(connector, CsvConnector)
        assert connector._file_path == './bici_estaciones/csv_manager/recorridos.csv'

    def test_reader(self):
        connector = CsvConnector('./bici_estaciones/csv_manager/recorridos.csv')
        assert isinstance(next(connector.reader), OrderedDict)
        assert next(connector.reader)['bici_id_usuario'] == '5453'
        connector = CsvConnector('./bici_estaciones/csv_manager/xxxxxxxxx.csv')
        with pytest.raises(FileNotFoundError):
            connector.reader


class TestRow:

    def test_creates(self):
        row = Row('station')
        assert isinstance(row, Row)
        assert row._start_station == 'station'

    def test_start_station(self):
        row = Row(' Station ')
        assert row.start_station == 'station'


class TestCsvFetcher:

    def test_creates(self):
        connector = CsvConnector('./bici_estaciones/csv_manager/recorridos.csv')
        fetcher = CsvFetcher(connector, '06:00:00', '11:59:00')
        assert isinstance(fetcher._filter_range_start, time)
        assert isinstance(fetcher._filter_range_end, time)

    def test_is_in_time_range(self):
        connector = CsvConnector('./bici_estaciones/csv_manager/recorridos.csv')
        fetcher = CsvFetcher(connector, '06:00:00', '11:59:00')
        assert fetcher._is_in_time_range('2018-01-01 09:31:00')
        assert not fetcher._is_in_time_range('2018-01-01 05:59:00')
        assert not fetcher._is_in_time_range('2018-01-01 12:00:00')

    def test_fetch_filtered(self):
        connector = CsvConnector('./bici_estaciones/csv_manager/recorridos.csv')
        fetcher = CsvFetcher(connector, '06:00:00', '11:59:00')
        rides = fetcher.fetch_filtered(3)
        assert isinstance(rides, list)
        assert len(rides) == 3

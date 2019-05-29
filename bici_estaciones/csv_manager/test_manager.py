from collections import OrderedDict

import pytest

from bici_estaciones.csv_manager.manager import CsvConnector


class TestCsvConnector:

    def test_creates(self):
        connector = CsvConnector('./bici_estaciones/csv_manager/recorridos.csv')
        assert isinstance(connector, CsvConnector)
        assert connector._file_path == './bici_estaciones/csv_manager/recorridos.csv'

    def test_reader(self):
        connector = CsvConnector('./bici_estaciones/csv_manager/recorridos.csv')
        assert isinstance(next(connector.reader), OrderedDict)
        assert next(connector.reader)['bici_id_usuario'] == '5453'
        connector1 = CsvConnector('./bici_estaciones/csv_manager/xxxxxxxxx.csv')
        with pytest.raises(FileNotFoundError):
            connector1.reader

from bici_estaciones.csv_manager.manager import CsvConnector, CsvFetcher

c = CsvConnector('./bici_estaciones/csv_manager/recorridos.csv')
fetcher = CsvFetcher(c, '06:00:00', '11:59:00')
print(fetcher.fetch_filtered())

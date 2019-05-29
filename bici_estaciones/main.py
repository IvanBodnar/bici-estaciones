from bici_estaciones.csv_manager.manager import CsvConnector, CsvFetcher

c = CsvConnector('./bici_estaciones/csv_manager/recorridos.csv')
fetcher = CsvFetcher(c, '06:00:00', '11:59:00')

for station in fetcher.fetch_filtered(3):
    print(station)

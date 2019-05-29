from bici_estaciones.csv_manager.manager import CsvConnector, CsvFetcher


def run():
    connector = CsvConnector('./bici_estaciones/csv_manager/recorridos.csv')
    fetcher = CsvFetcher(connector, '06:00:00', '11:59:00')
    print('Procesando los Datos...')
    for station in fetcher.fetch_filtered(3):
        print(station)


if __name__ == '__main__':
    run()

from bici_estaciones.business.station import Station


class TestStation:

    def test_creates(self):
        station = Station('congreso', 1000)
        assert isinstance(station, Station)
        assert station.departures_amount == 1000
        assert station.__repr__() == 'Estación: Congreso - Cantidad de Viajes: 1000'

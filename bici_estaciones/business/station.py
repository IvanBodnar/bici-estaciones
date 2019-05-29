
class Station:
    """
    Represents a station, used to organize the csv
    data, and yield a clean representation to print.
    """
    def __init__(self, name: str, departures_amount: int):
        self._name = name
        self._departures_amount = departures_amount

    @property
    def departures_amount(self):
        return self._departures_amount

    def __repr__(self):
        return f'Estación: {self._name.lower().capitalize()} - Cantidad de Viajes: {self._departures_amount}'

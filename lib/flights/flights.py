from .exceptions import FlightNotFound

class Flight:
    _all_flights = list()

    def __init__(self, flight_no, origin, dest):
        self.number = flight_no
        self.origin = origin
        self.destination = dest

    def __str__(self):
        return f"Flight Number {self.number} from {self.origin} to {self.destination}"

    @classmethod
    def search(cls, flight_no=None, origin_code=None, dest_code=None):
        results = list()
        for flight in cls._all_flights:
            if flight_no is not None and flight_no != flight.number:
                continue
            if origin_code is not None and origin_code != flight.origin:
                continue
            if dest_code is not None and dest_code != flight.destination:
                continue
            results.append(flight)
        return results

    @classmethod
    def new_flight(cls, flight_no, origin, dest):
        result = cls.search(flight_no, origin, dest)
        if result:
            return result[0]
        return cls(flight_no, origin, dest)

    @classmethod
    def edit_flight(cls, flight_no, origin, dest, new_number=None, new_origin=None, new_dest=None):
        results = cls.search(flight_no, origin, dest)
        if not results:
            raise FlightNotFound
        flight = results[0]
        flight.number = flight.number if new_number is None else new_number
        flight.origin = flight.origin if new_origin is None else new_origin
        flight.destination = flight.destination if new_origin is None else new_origin
        return flight

    @classmethod
    def delete_flight(cls, flight_no, origin, dest):
        target_index = None
        for i in range(len(cls._all_flights)):
            if cls._all_flights[i].number != flight_no:
                continue
            if cls._all_flights[i].origin != origin:
                continue
            if cls._all_flights[i].destination != dest:
                continue
            target_index = i
            break
        if target_index is None:
            return False
        cls._all_flights.pop(target_index)
        return True

    @classmethod
    def get_all(cls):
        return cls._all_flights

from typing import Optional
from lib.menu import Menu
from .exceptions import ReservationNotFound


class Reservation:
    _all_reservations = list()

    def __init__(self, flight, passenger):
        self.flight = flight
        self.passenger = passenger

    def __str__(self):
        return f"{self.passenger} on flight number {self.flight.number}"

    @classmethod
    def search(cls, flight=None, passenger=None) -> list:
        results = list()
        for res in cls._all_reservations:
            if flight is not None and res.flight != flight:
                continue
            if passenger is not None and res.passenger != passenger:
                continue
            results.append(res)
        return results

    @classmethod
    def new_booking(cls, flight, passenger):
        result = cls.search(flight, passenger)
        if result:
            return result[0]
        return cls(flight, passenger)

    @classmethod
    def change_booking(cls, flight, passenger, new_flight=None, new_passenger=None):
        results = cls.search(flight, passenger)
        if not results:
            raise ReservationNotFound
        booking = results[0]
        booking.flight = booking.flight if new_flight is None else new_flight
        booking.passenger = (
            booking.passenger if new_passenger is None else new_passenger
        )
        return booking

    @classmethod
    def delete_booking(cls, flight, passenger) -> bool:
        target_index = None
        for i in range(len(cls._all_reservations)):
            if cls._all_reservations[i].flight != flight:
                continue
            if cls._all_reservations[i].passenger != passenger:
                continue
            target_index = i
            break
        if target_index is None:
            return False
        cls._all_reservations.pop(target_index)
        return True

    @classmethod
    def get_all(cls):
        return cls._all_reservations

from typing import Optional

from lib.menu import Menu
from lib.reservations import Reservation
from lib.reservations.exceptions import ReservationNotFound
from lib.flights import Flight
from lib.flights.exceptions import FlightNotFound

def _input_flight_info(bare_values=False):
    try:
        number = input("Enter Flight Number: ")
        number = number if number else None
        origin = input("Enter Origin Code: ")
        origin = origin if origin else None
        dest = input("Enter Destination Code:")
        dest = dest if dest else None
    except KeyboardInterrupt:
        print("\nExit flight input.")
        return
    if bare_values:
        return number, origin, dest
    result = Flight.search(number, origin, dest)
    return result[0] if result else None

def _input_reservation_info(bare_values=False):
    flight = _input_flight_info()
    if flight is None:
        print("Flight not found.")
        return
    try:
        passenger = input("Enter passenger name: ")
        passenger = passenger if passenger else None
    except KeyboardInterrupt:
        print("Exit reservation input.")
        return
    if bare_values:
        return flight, passenger
    result = Reservation.search(flight=flight, passenger=passenger)
    return result[0] if result else None


def new_flight():
    number, origin, dest = _input_flight_info(bare_values=True)
    flight = Flight.new_flight(number, origin, dest)
    print(f"Flight created: {flight}")

def edit_flight():
    flight = _input_flight_info()
    if flight is None:
        print("Flight not found")
        return
    print("Enter new information. Blank values will not change.")
    number, origin, dest = _input_flight_info(bare_values=True)
    flight = Flight.edit_flight(
        flight.number,
        flight.origin,
        flight.destination,
        new_number=number,
        new_origin=origin,
        new_dest=dest)
    print(f"Flight updated: {flight}")


def list_flights():
    for flight in Flight.get_all():
        print(flight)


def delete_flight():
    flight = _input_flight_info()
    if flight is None:
        print("Flight not found.")
        return
    deleted = Flight.delete_flight(
        flight.number,
        flight.origin,
        flight.destination
    )
    if deleted:
        print("Flight deleted successfully.")
        return
    print("Something went wrong...")


def new_reservation():
    flight, passenger_name = _input_reservation_info(bare_values=True)
    res = Reservation.new_booking(flight, passenger_name)
    print(f"Booking submitted: {res}")


def edit_reservation():
    res = _input_reservation_info()
    if res is None:
        print("Reservation not found.")
        return
    print("Enter new information. Blank values will not change.")
    new_flight, new_passenger_name = _input_reservation_info(bare_values=True)
    Reservation.change_booking(
        res.flight,
        res.passenger,
        new_flight=new_flight,
        new_passenger=new_passenger_name)


def list_reservations():
    for res in Reservation.get_all():
        print(res)

def delete_reservation():
    res = _input_reservation_info()
    if res is None:
        print("reservation not found.")
        return
    deleted = Reservation.delete_booking(
        flight=res.flight,
        passenger=res.passenger)
    if deleted:
        print("Reservation successfully deleted")
        del res
        return
    print("Something went wrong...")


res_menu = Menu("Reservations Menu")
res_menu.new_option("n", "New Reservation", new_reservation)
res_menu.new_option("e", "Edit Reservation", edit_reservation)
res_menu.new_option("l", "List Reservations", list_reservations)
res_menu.new_option("d", "Delete Reservation", delete_reservation)

flight_menu = Menu("Flights Menu")
flight_menu.new_option("n", "New Flight", new_flight)
flight_menu.new_option("e", "Edit Flight", edit_flight)
flight_menu.new_option("l", "List Flights", list_flights)
flight_menu.new_option("d", "Delete Flight", delete_flight)

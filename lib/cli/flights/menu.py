from lib.menu import Menu
from lib.flights import Flight

__all__ = ["flight_menu"]

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
        new_dest=dest,
    )
    print(f"Flight updated: {flight}")


def list_flights():
    for flight in Flight.get_all():
        print(flight)


def delete_flight():
    flight = _input_flight_info()
    if flight is None:
        print("Flight not found.")
        return
    deleted = Flight.delete_flight(flight.number, flight.origin, flight.destination)
    if deleted:
        print("Flight deleted successfully.")
        return
    print("Something went wrong...")


def _setup_flight_menu():
    menu = Menu("Flights Menu")
    menu.new_option("n", "New Flight", new_flight)
    menu.new_option("e", "Edit Flight", edit_flight)
    menu.new_option("l", "List Flights", list_flights)
    menu.new_option("d", "Delete Flight", delete_flight)
    return menu


flight_menu = _setup_flight_menu()

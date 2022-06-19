from lib.cli.flights.menu import _input_flight_info
from lib.menu import Menu
from lib.reservations import Reservation


__all__ = ["res_menu"]

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
        new_passenger=new_passenger_name,
    )


def list_reservations():
    for res in Reservation.get_all():
        print(res)


def delete_reservation():
    res = _input_reservation_info()
    if res is None:
        print("reservation not found.")
        return
    deleted = Reservation.delete_booking(flight=res.flight, passenger=res.passenger)
    if deleted:
        print("Reservation successfully deleted")
        del res
        return
    print("Something went wrong...")


def setup_reservation_menu():
    menu = Menu("Reservations Menu")
    menu.new_option("n", "New Reservation", new_reservation)
    menu.new_option("e", "Edit Reservation", edit_reservation)
    menu.new_option("l", "List Reservations", list_reservations)
    menu.new_option("d", "Delete Reservation", delete_reservation)
    return menu


res_menu = setup_reservation_menu()

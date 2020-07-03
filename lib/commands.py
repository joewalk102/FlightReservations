from lib.menu import Menu


def new_flight():
    pass


def edit_flight():
    pass


def delete_flight():
    pass


def new_reservation():
    pass


def edit_reservation():
    flight_no = input("Enter flight number: ")
    res_no = input("Enter Reservation Number: ")


def delete_reservation():
    pass


res_menu = Menu("Reservations Menu")
res_menu.new_option("n", "New Reservation", new_reservation)
res_menu.new_option("e", "Edit Reservation", edit_reservation)
res_menu.new_option("d", "Delete Reservation", delete_reservation)

flight_menu = Menu("Flights Menu")
flight_menu.new_option("n", "New Flight", new_flight)
flight_menu.new_option("e", "Edit Flight", edit_flight)
flight_menu.new_option("d", "Delete Flight", delete_flight)

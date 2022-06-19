from lib.menu import Menu
from lib.cli.reservations.menu import res_menu
from lib.cli.flights.menu import flight_menu

menu = Menu("Main Menu")
menu.new_option("r", "Reservations", res_menu.prompt)
menu.new_option("f", "Flights", flight_menu.prompt)


def main():
    print("Welcome to the flight reservation system.")
    try:
        menu.prompt()
    except KeyboardInterrupt:
        pass
    print("\n\nExiting...\n\n")


if __name__ == "__main__":
    main()

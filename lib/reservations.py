from lib.menu import Menu


class Reservation:
    _all_reservations = list()

    def __init__(self):
        self.flight = ""
        self.passenger = ""

    @classmethod
    def new_booking(cls):
        pass

    @classmethod
    def change_booking(cls):
        pass

    @classmethod
    def delete_booking(cls):
        pass

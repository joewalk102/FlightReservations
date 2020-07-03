class Flight:
    def __new__(cls, *args, **kwargs):
        return super(Flight, cls).__new__(*args, **kwargs)

    def __init__(self):
        self.number = ""
        self.origin = ""
        self.destination = ""

    @classmethod
    def list_flights(cls, flight_no=None, origin_code=None, dest_code=None):
        """
        Get a list of all flights that match the given search terms.

        Args:
            flight_no:
            origin_code:
            dest_code:

        Return:

        """
        pass

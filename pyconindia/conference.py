"""
Conference Actions
"""

class Conference:
    def __init__(self):
        return

    def year(self):
        return self.__get_current_year()

    def location(self, year=None):
        if not year:
            year = self.__get_current_year()
        return self.__get_current_location(year)

    def cfp(self, year=None):
        if not year:
            year = self.__get_current_year()
        return self.__get_cfp_status(year)

    def __get_current_year(self):
        year = 2021
        return year

    def __get_current_location(self, year):
        # TODO: get location data from year wise yaml file
        location = "Anywhere on Earth"
        return location

    def __get_cfp_status(self, year):
        # TODO: get cfp state based on year
        cfp_text = "Submit your proposal: https://in.pycon.org/cfp/2021/proposals/"
        return cfp_text

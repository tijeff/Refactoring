# Copyright 2014 Epitez
#
# All Rights Reserved.

"""
Rentals...
"""


# =============================================================================
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# =============================================================================
class Rental:
    def __init__(self, movie, days_rented):
        self._movie = movie
        self._daysRented = days_rented

    def get_days_rented(self):
        return self._daysRented

    def get_movie(self):
        return self._movie


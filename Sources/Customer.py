# Copyright 2014 Epitez
#
# All Rights Reserved.

"""
Customers...
"""


# =============================================================================
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# =============================================================================
from .Movie import Movie


class Customer:
    def __init__(self, name):
        self._name = name
        self._rentals = list()

    def add_rental(self, arg):
        self._rentals.append(arg)

    def get_name(self):
        return self._name

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0
        result = "Dossier de location de " + self.get_name() + "\n"
        for each in self._rentals:
            this_amount = 0

            # Determine amounts for each line
            if each.get_movie().get_price_code() == Movie.REGULAR:
                this_amount += 2
                if each.get_days_rented() > 2:
                    this_amount += each.get_days_rented() * 3
            elif each.get_movie().get_price_code() == Movie.NEW_RELEASE:
                this_amount += each.get_days_rented() * 3
            elif each.get_movie().get_price_code() == Movie.CHILDREN:
                this_amount += 1.5
                if each.get_days_rented() > 3:
                    this_amount += (each.get_days_rented()-3)*1.5

            # Add frequent renter points
            frequent_renter_points += 1

            # Add bonus
            if (each.get_movie().get_price_code() == Movie.NEW_RELEASE) and each.get_days_rented() > 1:
                frequent_renter_points += 1

            # show figures for this rental
            result += "\t" + each.get_movie().get_title() + "\t" + str(this_amount) + "\n"

            total_amount += this_amount

        # Add footer lines
        result += "Le montant dû est de " + str(total_amount) + "\n"
        result += "Vous avez gagné " + str(frequent_renter_points) + " frequent renter points"
        return result

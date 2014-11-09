# Copyright 2014 Epitez
#
# All Rights Reserved.

"""
Movies...
"""


# =============================================================================
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# =============================================================================
class Movie:
    CHILDREN = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, price_code):
        self._title = title
        self._priceCode = price_code

    def get_title(self):
        return self._title


    def set_price_code(self, price_code):
        self._priceCode = price_code


    def get_price_code(self):
        return self._priceCode

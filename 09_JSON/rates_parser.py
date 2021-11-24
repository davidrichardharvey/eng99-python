import json

class RatesParser:
    pass

# On initialisation, read in a provided filepath
# Base, date, GBP, USD and AUD rates
# e.g. self.gbp = <0.89275>
# self.rates = <dictionary of all the rates>
# Method called convert
# Takes in a string corresponding to a currency
# Takes in a value (representing EUR)
# Returns the value in the other currency

# Think about how the convert method should handle being
# passed a currency not found in the json file

"""Print out all the melons in our inventory."""

#these are dictionaries
from melons import (melon_names, melon_seedlessness, melon_prices,
                    melon_flesh_color, melon_rind_color, melon_avg_weight)


def gather_melon_data():
    """Gathers melon data from melons.py.

        Create one dictionary with all the desired values
        key is melon type
        values are a tuple with:
        (price, seedlessness, flesh color, rind color, avg weight)
        """
    #create an empty dictionary to hold all the melon data
    melon_data = {}

    #iterate through the three dictionaries and put the data into melon_data
    #first, get the melon names
    for i in melon_names:
        melon_data[melon_names[i]] = tuple([melon_prices.get(i, 0),
                                            melon_seedlessness.get(i, 'unknown'),
                                            #not sure how to do this if they don't exist
                                            #tried to use get, but failed
                                            melon_flesh_color.get(i, 'unknown'),
                                            melon_rind_color.get(i, 'unknown'),
                                            melon_avg_weight.get(i, 'unknown')])
    return melon_data


def print_melon(melon_dict):
    """Prints the melon data from the melon dictionary."""

    for melon, info in melon_dict.items():
        print """%s
        seedless: %s
        price: %d
        flesh_color:  %s
        weight: %s
        rind_color: %s""" % (melon, info[1],
                             info[0], info[2],
                             info[4], info[3])

print_melon(gather_melon_data())

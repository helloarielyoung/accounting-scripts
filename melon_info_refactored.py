"""Print out all the melons in our inventory."""

#these are dictionaries
from melons_refactored import melon_data


def print_melon(melon_data):
    """Prints the melon data from the melon dictionary.

    Given a dictionary of melon data in the following format,
    this function will print the melon data.

    Dictionary contains 
        Key: melon name
        Value: tuple with (price,
                            seedlessness
                            flesh_color
                            rind_color
                            avg_weight)

    """

    for melon, info in melon_data.items():
        print """%s
        seedless: %s
        price: %d
        flesh_color:  %s
        weight: %s
        rind_color: %s""" % (melon, info[1],
                             info[0], info[2],
                             info[4], info[3])

print_melon(melon_data)

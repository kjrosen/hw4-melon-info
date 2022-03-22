"""Print out all the melons in our inventory."""


from melons import melon_deets 


def print_melon(melons):
    """Print each melon with corresponding attribute information.
    
    Parameter is a dictionary
    """

    for melon in melons:
        print(melon)

        for deets in melons[melon]:
            print(deets, ":", melons[melon][deets])

        print()

print_melon(melon_deets)
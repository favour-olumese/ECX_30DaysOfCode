# ECX 30 DAYS OF CODE AND DESIGN
# Day 6

"""
**Man in the Well**

A man is stuck at the bottom of a well. Each day, he climbs up 8 metres, and then at night, he slips 3 metres.
Using loop (any loop of your choice), write a function to determine and print how long he takes to climb out of a well
of any given depth, where the depth of the well is taken as input.
"""


def day_in_well(well_height):
    """This determines the number of days, it takes for the man to climb out of the well"""

    still_in_well = True

    day = 1
    climb_height = 0

    while still_in_well is True:

        if well_height <= 0:
            print('He was never in the well.')
            break

        # The climbing height during the day.
        climb_height = climb_height + 8

        if climb_height < well_height:
            day = day + 1

            # The falling at night.
            climb_height = climb_height - 3

        else:
            print('He took about %d day(s) to get out of the well' % day)
            still_in_well = False


# Function call
day_in_well(17)

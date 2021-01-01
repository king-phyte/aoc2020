"""
--- Part Two ---

Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list.
However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft,
so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
s
"""

from part_1 import find_seat_id


def main():
    with open("./input.txt") as f:
        puzzle_input = f.readlines()

    seat_ids = [find_seat_id(seat.strip()) for seat in puzzle_input]

    for i in range(len(seat_ids)):
        if i not in seat_ids and i > 39:
            print(i)


if __name__ == '__main__':
    main()

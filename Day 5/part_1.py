"""
--- Day 5: Binary Boarding ---

You board your plane only to discover a new problem: you dropped your boarding pass!
You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that
suddenly made it through passport control.

You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input);
perhaps you can find your seat through process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like
FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane
(numbered 0 through 127). Each letter tells you which half of a region the given seat is in.
Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63)
or the back (64 through 127). The next letter indicates which half of that region the seat is in,
and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.

The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane
(numbered 0 through 7). The same process as above proceeds again, this time with only three steps.
L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

    Start by considering the whole range, columns 0 through 7.
    R means to take the upper half, keeping columns 4 through 7.
    L means to take the lower half, keeping columns 4 through 5.
    The final R keeps the upper of the two, column 5.

So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column.
In this example, the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.

As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

"""
from typing import List


def find_row(characters: str) -> int:
    """
    Find the specific row in the airplane from the code (characters).
    There are 128 rows in total.
    The characters that determine the specific row are F (front) and B (back).
        - If a character is F, the lower half of the seats are taken.
        - If a character is B, the upper half of the seats remaining are taken.
    The function returns the last number in the list of rows.

    :param characters: str
    :return: int - Specific row
    """
    rows: List[int] = [i for i in range(128)]
    for char in characters:
        midpoint = int(len(rows) / 2)
        if char == "F":
            rows = rows[:midpoint]
        elif char == "B":
            rows = rows[midpoint:]
    return rows[0]


def find_column(characters: str) -> int:
    """
    Find the specific column in the airplane from the code (characters).
    There are 8 columns in total.
    The characters that determine the specific row are L (left) and R (right).
        - If a character is L, the lower half of the seats remaining are taken.
        - If a character is R, the upper half of the seats remaining are taken.
    The function returns the last number in the list of columns.

    :param characters: str
    :return: int - Specific column
    """
    columns: List[int] = [i for i in range(8)]
    for char in characters:
        midpoint = int(len(columns) / 2)
        if char == "L":
            columns = columns[:midpoint]
        elif char == "R":
            columns = columns[midpoint:]
    return columns[0]


def find_seat_id(characters: str) -> int:
    """
    The function returns the seat ID given the code (characters).
    The seat ID is obtained by multiplying the row by 8, then adding the column.

    :param characters: str
    :return: int - Seat ID
    """
    row = find_row(characters[:8])
    column = find_column(characters[-3:])

    return (row * 8) + column


def main():
    with open("./input.txt") as f:
        puzzle_input = f.readlines()

    seat_ids = [find_seat_id(seat.strip()) for seat in puzzle_input]
    print(max(seat_ids))  # Answer: 980


if __name__ == '__main__':
    main()

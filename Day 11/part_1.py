"""
--- Day 11: Seating System ---

Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the
tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you
realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can
predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#).
For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and
always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat
(one of the eight positions immediately up, down, left, right, or diagonal from the seat).
The following rules are applied to every seat simultaneously:

    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##

This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##

#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##

#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##

At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no
seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state.
How many seats end up occupied?

"""
from typing import List, Sequence


def switches(matrix: Sequence[Sequence[str]]) -> List[List[str]]:
    """
    Makes an array out of each seat surrounding the current seat and checks to see if there is >= 4 or 0
    occupied seats and updates the seats as needed.

    :param matrix:
    :return: List[List[str]] - New Matrix
    """
    new_matrix = []
    for (i, x) in enumerate(matrix):
        new_row = []
        for (j, y) in enumerate(x):
            adjacent_seats = [
                matrix[i - 1][j - 1] if ((i - 1 >= 0) and (j - 1 >= 0)) else None,
                matrix[i - 1][j] if (i - 1 >= 0) else None,
                matrix[i - 1][j + 1] if ((i - 1 >= 0) and (j + 1 < len(x))) else None,
                matrix[i][j - 1] if (j - 1 >= 0) else None,
                matrix[i][j + 1] if (j + 1 < len(x)) else None,
                matrix[i + 1][j - 1] if (i + 1 < len(matrix) and (j - 1 >= 0)) else None,
                matrix[i + 1][j] if (i + 1 < len(matrix)) else None,
                matrix[i + 1][j + 1] if (i + 1 < len(matrix) and (j + 1 < len(x))) else None
            ]
            if (adjacent_seats.count("#") >= 4) and (y == "#"):
                new_row.append("L")
            elif (adjacent_seats.count("#") == 0) and (y == "L"):
                new_row.append("#")
            else:
                new_row.append(y)
        new_matrix.append(new_row)
    return new_matrix


def switch_loop(matrix: Sequence[Sequence[str]], old_matrix: Sequence[Sequence[str]]) -> List[List[str]]:
    """
    Loops through permutations until we get the same seating arrangement twice.
    Returns the matrix if it is equal to the old matrix.

    :param matrix:
    :param old_matrix:
    :return:  List[List[str]] - Matrix
    """
    return matrix if (matrix == old_matrix) else switch_loop(switches(matrix), matrix)


def occupied_seats(data: Sequence[str]) -> int:
    """
    Returns the number of # in the final matrix
    :param data: Puzzle input - Sequence[str]
    :return: Number of # found - int
    """
    matrix = [list(x) for x in data]
    final_matrix = switch_loop(switches(matrix), matrix)

    return sum(x.count("#") for x in final_matrix)


def main():
    with open("input.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print(occupied_seats(puzzle_input))  # Answer = 2418


if __name__ == '__main__':
    main()

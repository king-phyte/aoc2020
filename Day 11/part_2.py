"""
--- Part Two ---

As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats
They care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight
directions. For example, the empty seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....

The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

.............
.L.L.#.#.#.#.
.............

The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.

Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an
occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply:
empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

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

#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#

#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs,
you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached,
how many seats end up occupied?

"""
from typing import List


def switches(matrix):
    new_matrix = []
    for (i, x) in enumerate(matrix):
        new_row = []
        for (j, y) in enumerate(x):
            left = list(reversed(x[:j]))
            right = x[j + 1:]
            up = [matrix[i - k][j] for k in range(1, i + 1)]
            down = [matrix[k][j] for k in range(i + 1, len(matrix))]
            up_left = list(filter(lambda g: g, [matrix[i - k][j - k] if j - k >= 0 else None for k in range(1, i + 1)]))
            up_right = list(
                filter(lambda g: g, [matrix[i - k][j + k] if j + k < len(x) else None for k in range(1, i + 1)]))
            down_left = list(filter(
                lambda g: g, [matrix[i + k][j - k] if j - k >= 0 else None for k in range(1, len(matrix) - i)]))
            down_right = list(filter(
                lambda g: g, [matrix[i + k][j + k] if j + k < len(x) else None for k in range(1, len(matrix) - i)]))
            directions = [left, right, up, down, up_left, up_right, down_left, down_right]
            first_seats = []
            for d in directions:
                first_seat = [f for f in d if f != "."][0:1]
                first_seats.append("".join(first_seat))

            if (first_seats.count("#") >= 5) and (y == "#"):
                new_row.append("L")
            elif (first_seats.count("#") == 0) and (y == "L"):
                new_row.append("#")
            else:
                new_row.append(y)
        new_matrix.append(new_row)
    return new_matrix


def switch_loop(matrix: List[List[str]], old_matrix: List[list]) -> List[List[str]]:
    """
    Loops through permutations until we get the same seating arrangement twice.
    """
    if matrix == old_matrix:
        return matrix
    else:
        return switch_loop(switches(matrix), matrix)


def occupied_seats(data: List[str]) -> int:
    """
    Makes an array of arrays of every seat on the diagonal then it finds the first seat in each seat array.
    Then it counts the number of occupied seats and updates.
    """
    matrix = [list(x) for x in data]
    final_matrix = switch_loop(switches(matrix), matrix)

    return sum(x.count("#") for x in final_matrix)


def main():
    with open("./input.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print(occupied_seats(puzzle_input))  # Answer = 2144s


if __name__ == '__main__':
    main()

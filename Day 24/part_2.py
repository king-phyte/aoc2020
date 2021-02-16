"""
--- Part Two ---

The tile floor in the lobby is meant to be a living art exhibit.
Every day, the tiles are all flipped according to the following rules:

    Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
    Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.

Here, tiles immediately adjacent means the six tiles directly touching the tile in question.

The rules are applied simultaneously to every tile; put another way, it is first determined which tiles need to be
flipped, then they are all flipped at the same time.

In the above example, the number of black tiles that are facing up after the given number of days has passed is as
follows:

Day 1: 15
Day 2: 12
Day 3: 25
Day 4: 14
Day 5: 23
Day 6: 28
Day 7: 41
Day 8: 37
Day 9: 49
Day 10: 37

Day 20: 132
Day 30: 259
Day 40: 406
Day 50: 566
Day 60: 788
Day 70: 1106
Day 80: 1373
Day 90: 1844
Day 100: 2208

After executing this process a total of 100 times, there would be 2208 black tiles facing up.

How many tiles will be black after 100 days?

"""
from collections import Counter
from typing import Set, Tuple

from part_1 import tiles_with_black_side_up


def hexagonal_neighbours(right: int, center: int) -> Set[Tuple[int, int]]:
    neighbours = {(right, center + 1), (right, center - 1)}

    if right % 2:
        neighbours |= {(right + 1, center - 1), (right + 1, center), (right - 1, center - 1), (right - 1, center)}
    else:
        neighbours |= {(right + 1, center), (right + 1, center + 1), (right - 1, center + 1), (right - 1, center)}

    return neighbours


def black_tiles_after_days(tiles: Set[Tuple[int, int]], days: int) -> Set[Tuple[int, int]]:
    for _ in range(days):
        c = Counter()

        for x, y in tiles:
            for ny, nx in hexagonal_neighbours(y, x):
                c[(nx, ny)] += 1

        tiles = {
            coordinates for coordinates in c if c[coordinates] == 2 or (coordinates in tiles and c[coordinates] == 1)
        }

    return tiles


def main():
    with open("./input.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    tiles = tiles_with_black_side_up(puzzle_input)
    days = 100
    black_tiles_after_100_days = black_tiles_after_days(tiles, days)
    print(len(black_tiles_after_100_days))  # Answer = 3627


if __name__ == '__main__':
    main()

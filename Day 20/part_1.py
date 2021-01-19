"""
--- Day 20: Jurassic Jigsaw ---

The high-speed train leaves the forest and quickly carries you south. You can even see a desert in the distance!
Since you have some spare time, you might as well see if there was anything interesting in the image the
Mythical Information Bureau satellite captured.

After decoding the satellite messages, you discover that the data actually contains many small images created by the
satellite's camera array. The camera array consists of many cameras; rather than produce a single square image,
they produce many smaller square image tiles that need to be reassembled back into a single image.

Each camera in the camera array returns a single monochrome image tile with a random unique ID number. The tiles
(your puzzle input) arrived in a random order.

Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and flipped to a random
orientation. Your first task is to reassemble the original image by orienting the tiles so they fit together.

To show how the tiles should be reassembled, each tile's image data includes a border that should line up exactly with
its adjacent tiles. All tiles have this border, and the border lines up exactly when the tiles are both
oriented correctly. Tiles at the edge of the image also have this border, but the outermost edges won't line up
with any other tiles.

For example, suppose you have the following nine tiles:

Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...

By rotating, flipping, and rearranging them, you can find a square arrangement that causes
all adjacent borders to line up:

#...##.#.. ..###..### #.#.#####.
..#.#..#.# ###...#.#. .#..######
.###....#. ..#....#.. ..#.......
###.##.##. .#.#.#..## ######....
.###.##### ##...#.### ####.#..#.
.##.#....# ##.##.###. .#...#.##.
#...###### ####.#...# #.#####.##
.....#..## #...##..#. ..#.###...
#.####...# ##..#..... ..#.......
#.##...##. ..##.#..#. ..#.###...

#.##...##. ..##.#..#. ..#.###...
##..#.##.. ..#..###.# ##.##....#
##.####... .#.####.#. ..#.###..#
####.#.#.. ...#.##### ###.#..###
.#.####... ...##..##. .######.##
.##..##.#. ....#...## #.#.#.#...
....#..#.# #.#.#.##.# #.###.###.
..#.#..... .#.##.#..# #.###.##..
####.#.... .#..#.##.. .######...
...#.#.#.# ###.##.#.. .##...####

...#.#.#.# ###.##.#.. .##...####
..#.#.###. ..##.##.## #..#.##..#
..####.### ##.#...##. .#.#..#.##
#..#.#..#. ...#.#.#.. .####.###.
.#..####.# #..#.#.#.# ####.###..
.#####..## #####...#. .##....##.
##.##..#.. ..#...#... .####...#.
#.#.###... .##..##... .####.##.#
#...###... ..##...#.. ...#..####
..#.#....# ##.#.#.... ...##.....

For reference, the IDs of the above tiles are:

1951    2311    3079
2729    1427    2473
2971    1489    1171

To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together.
If you do this with the assembled tiles from the example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.

Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?

"""
from functools import reduce
from collections import defaultdict
from itertools import product
from typing import Sequence, Dict, Tuple, List, Union, DefaultDict, Any


def digits_in(line: str) -> Union[List[int], list]:
    result = []
    for char in line:
        if char.isdigit():
            result.append(char)

    return [int("".join(result))] if result else []


def find_edges(tile: Sequence[str]) -> Tuple[str, str, str, str]:
    first = "".join(tile[0])
    last = "".join(tile[-1])
    first_in_row = []
    last_in_row = []
    for row in range(len(tile)):
        first_in_row.append(tile[row][0])
        last_in_row.append(tile[row][-1])
    return first, last, "".join(first_in_row), "".join(last_in_row)


def multiply_all(numbers: Sequence[int]) -> int:
    return reduce(lambda x, y: x * y, numbers)


def matches(x: str, y: str) -> bool:
    return (x == y) or (x == "".join(reversed(y)))


def find_id_of_corners(corners: Dict[int, int]):
    return [k for k, v in corners.items() if v == 2]


def find_corner_tiles(tiles: Dict[int, Sequence[str]]) -> DefaultDict[Any, int]:
    sides = {}
    tiles_and_number_of_matches = defaultdict(int)

    for tile_id, tile in tiles.items():
        sides[tile_id] = find_edges(tile)

    for a, b in product(sides.keys(), repeat=2):
        if a == b:
            continue

        for a_side, b_side in product(sides[a], sides[b]):
            if matches(a_side, b_side):
                tiles_and_number_of_matches[a] += 1

    return tiles_and_number_of_matches


def parse_input(data: Sequence[str]) -> Dict[int, List[str]]:
    tiles = {}
    tile = []
    tile_id = -1

    for line in data:
        if line.strip():
            if digits_in(line):
                tile_id = digits_in(line)[0]
            else:
                tile.append(line.strip())
        else:
            tiles[tile_id] = tile
            tile_id = -1
            tile = []

    return tiles


def main():
    with open("./input.txt") as f:
        puzzle_input = f.readlines()

    tiles = parse_input(puzzle_input)

    four_corners = find_corner_tiles(tiles)
    id_of_corners = find_id_of_corners(four_corners)
    print(multiply_all(id_of_corners))  # Answer = 84_116_744_709_593


if __name__ == '__main__':
    main()

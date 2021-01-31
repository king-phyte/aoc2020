"""
--- Part Two ---

Now, you're ready to check the image for sea monsters.

The borders of each tile are not part of the actual image; start by removing them.

In the example above, the tiles become:

.#.#..#. ##...#.# #..#####
###....# .#....#. .#......
##.##.## #.#.#..# #####...
###.#### #...#.## ###.#..#
##.#.... #.##.### #...#.##
...##### ###.#... .#####.#
....#..# ...##..# .#.###..
.####... #..#.... .#......

#..#.##. .#..###. #.##....
#.####.. #.####.# .#.###..
###.#.#. ..#.#### ##.#..##
#.####.. ..##..## ######.#
##..##.# ...#...# .#.#.#..
...#..#. .#.#.##. .###.###
.#.#.... #.##.#.. .###.##.
###.#... #..#.##. ######..

.#.#.### .##.##.# ..#.##..
.####.## #.#...## #.#..#.#
..#.#..# ..#.#.#. ####.###
#..####. ..#.#.#. ###.###.
#####..# ####...# ##....##
#.##..#. .#...#.. ####...#
.#.###.. ##..##.. ####.##.
...###.. .##...#. ..#..###

Remove the gaps to form the actual image:

.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###

Now, you're ready to search for sea monsters! Because your image is monochrome, a sea monster will look like this:

                  #
#    ##    ##    ###
 #  #  #  #  #  #

When looking for this pattern in the image, the spaces can be anything; only the # need to match. Also,
you might need to rotate or flip your image before it's oriented correctly to find sea monsters. In the above image,
after flipping and rotating it to the appropriate orientation, there are two sea monsters (marked with O):

.####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.O#..
#.O.##.OO#.#.OO.##.OOO##
..#O.#O#.O##O..O.#O##.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.##O###.
.O##.#OO.###OO##..OOO##.
..O#.O..O..O.#O##O##.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#

Determine how rough the waters are in the sea monsters' habitat by counting the number of # that are not part of a
sea monster. In the above example, the habitat's water roughness is 273.

How many # are not part of a sea monster?

"""
import re
from collections import defaultdict
from itertools import product
from typing import Dict, List, Sequence, Set, Tuple
from part_1 import matches, find_edges

MONSTER = (
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
)


def find_integers(line: str) -> List[int]:
    pattern = re.compile(r'-?\d+')

    return [int(val) for val in re.findall(pattern, line) if val]


def flip_vertically(image: Sequence[Sequence[str]]) -> Tuple[Tuple[str], ...]:
    return tuple(tuple(row) for row in image[::-1])


def rotate(image: Sequence[str]) -> Tuple[Tuple[str]]:
    rotated_image = []
    row = []

    for x in range(len(image[0])):
        for y in range(len(image)):
            row.append(image[y][x])
        rotated_image.append(row[::-1])
        row = []

    if row:
        rotated_image.append(row)

    return tuple(tuple(row) for row in rotated_image)


def flip_turns(image: Tuple[str, str, str]) -> Set[Tuple[Tuple[str, ...], ...]]:
    flipped_turn = set()

    for _ in range(4):
        image = rotate(image)
        flipped_turn.add(image)
        flipped_turn.add(flip_vertically(image))

    return flipped_turn


def count_monsters(image: Sequence[Sequence[str]]) -> int:
    monster_flips = flip_turns(MONSTER)

    squares = {(y, x) for y in range(len(image)) for x in range(len(image[0])) if image[y][x] == '#'}
    monstered = set()

    height = len(image)
    width = len(image[0])

    for monster in monster_flips:
        monster_height = len(monster)
        monster_width = len(monster[0])

        for y in range(height - monster_height + 1):
            for x in range(width - monster_width + 1):
                match = True
                hit = set()

                for dy in range(monster_height):
                    for dx in range(monster_width):
                        if monster[dy][dx] != '#':
                            continue
                        if image[y + dy][x + dx] != '#':
                            match = False
                        else:
                            hit.add((y + dy, x + dx))

                if match:
                    monstered |= hit

    return len(squares - monstered)


def find_monsters(tiles: Dict[int, Sequence[str]]) -> List[List[str]]:
    sides = {}

    for tile_id, tile in tiles.items():
        sides[tile_id] = find_edges(tile)

    graph = defaultdict(list)

    for a, b in product(sides.keys(), repeat=2):
        if a == b:
            continue

        for a_side, b_side in product(sides[a], sides[b]):
            if matches(a_side, b_side):
                graph[a].append(b)

    corners = [k for k, v in graph.items() if len(v) == 2]

    image = {corners[0]: (0, 0)}
    node = corners[0]
    y = 0
    x = 1
    corner_count = 1

    while any((n not in image and len(graph[n]) < 4) for n in graph[node]):
        for neighbour in graph[node]:
            if (neighbour not in image) and (len(graph[neighbour]) < 4):
                image[neighbour] = (y, x)
                node = neighbour

                if len(graph[node]) == 2:
                    corner_count += 1

                if corner_count == 1:
                    x += 1
                elif corner_count == 2:
                    y += 1
                elif corner_count == 3:
                    x -= 1
                elif corner_count == 4:
                    y -= 1

                break

    height = max(val[0] for val in image.values()) + 1
    width = max(val[1] for val in image.values()) + 1

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            left = [k for k, v in image.items() if v == (y, x - 1)][0]
            up = [k for k, v in image.items() if v == (y - 1, x)][0]

            intersection = [
                tile_id for tile_id in graph.keys() if (tile_id in graph[left])
                and (tile_id in graph[up])
                and (tile_id not in image)][0]

            image[intersection] = (y, x)

    coord_to_id = {v: k for k, v in image.items()}

    tile_height = len(tiles[corners[0]])
    tile_width = len(tiles[corners[0]][0])

    canvas = [[' ' for _ in range((tile_width - 2) * width)] for _ in range((tile_height - 2) * height)]

    for y in range(height):
        for x in range(width):
            tile_id = coord_to_id[(y, x)]
            tile = tiles[tile_id]

            up, down, left, right = find_edges(tile)

            if x < width - 1:
                right_tile_id = coord_to_id[(y, x + 1)]
                right_tile = tiles[right_tile_id]
                right_tile_edges = find_edges(right_tile)

                while not any(matches(right, edge) for edge in right_tile_edges):
                    tile = rotate(tile)
                    up, down, left, right = find_edges(tile)

            else:
                left_tile_id = coord_to_id[(y, x - 1)]
                left_tile = tiles[left_tile_id]
                left_tile_edges = find_edges(left_tile)

                while not any(matches(left, edge) for edge in left_tile_edges):
                    tile = rotate(tile)
                    up, down, left, right = find_edges(tile)

            if y < height - 1:
                down_tile_id = coord_to_id[(y + 1, x)]
                down_tile = tiles[down_tile_id]
                down_tile_edges = find_edges(down_tile)

                if not any(matches(down, edge) for edge in down_tile_edges):
                    tile = flip_vertically(tile)

            else:
                up_tile_id = coord_to_id[(y - 1, x)]
                up_tile = tiles[up_tile_id]
                up_tile_edges = find_edges(up_tile)

                if not any(matches(up, edge) for edge in up_tile_edges):
                    tile = flip_vertically(tile)

            start_y = y * (tile_height - 2)
            start_x = x * (tile_width - 2)

            for dy in range(tile_height - 2):
                for dx in range(tile_width - 2):
                    canvas[start_y + dy][start_x + dx] = tile[dy + 1][dx + 1]

    return canvas


def parse_input(data: Sequence[str]) -> Dict[int, List[str]]:
    """
    Parses the input into a dictionary of numbers (tile IDs) and tiles
    """
    tiles = {}
    tile = []
    tile_id = -1

    for line in data:
        if line.strip():
            if find_integers(line):
                tile_id = find_integers(line)[0]
            else:
                tile.append(line.strip())
        else:
            tiles[tile_id] = tile
            tile_id = -1
            tile = []

    tiles[tile_id] = tile
    return tiles


def main():
    with open("./input.txt") as f:
        puzzle_input = f.readlines()

    tiles = parse_input(puzzle_input)

    canvas = find_monsters(tiles)
    print(count_monsters(canvas))  # Answer = 1957


if __name__ == '__main__':
    main()

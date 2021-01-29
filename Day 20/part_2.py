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
from typing import Dict, List, Sequence, Tuple

from part_1 import matches, find_edges

MONSTER = (
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
)


def ints(line):
    pattern = re.compile(r'-?\d+')

    return [int(val) for val in re.findall(pattern, line) if val]


def flip_y(image):
    return tuple(tuple(row) for row in image[::-1])


def rotate(image: Sequence[str]):
    im = []
    row = []

    for x in range(len(image[0])):
        for y in range(len(image)):
            row.append(image[y][x])
        im.append(row[::-1])
        row = []

    if row:
        im.append(row)

    a = tuple(tuple(row) for row in im)
    print(a)
    return a


def flipturns(image):
    out = set()

    for _ in range(4):
        image = rotate(image)
        out.add(image)
        out.add(flip_y(image))

    return out


def count_monsters(image):
    monsterflips = flipturns(MONSTER)

    squares = {(y, x) for y in range(len(image)) for x in range(len(image[0])) if image[y][x] == '#'}
    monstered = set()

    height = len(image)
    width = len(image[0])

    for m in monsterflips:
        mheight = len(m)
        mwidth = len(m[0])

        for y in range(height - mheight + 1):
            for x in range(width - mwidth + 1):
                match = True
                hit = set()

                for dy in range(mheight):
                    for dx in range(mwidth):
                        if m[dy][dx] != '#':
                            continue
                        if image[y + dy][x + dx] != '#':
                            match = False
                        else:
                            hit.add((y + dy, x + dx))

                if match:
                    monstered |= hit

    return len(squares - monstered)


def solve(tiles: Dict[int, Sequence[str]]) -> int:
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

            intersection = [tile_id for tile_id in graph.keys()
                            if (tile_id in graph[left]) and (tile_id in graph[up]) and (tile_id not in image)][0]

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
                did = coord_to_id[(y + 1, x)]
                dtile = tiles[did]
                dedges = find_edges(dtile)

                if not any(matches(down, edge) for edge in dedges):
                    tile = flip_y(tile)
            else:
                uid = coord_to_id[(y - 1, x)]
                utile = tiles[uid]
                uedges = find_edges(utile)

                if not any(matches(up, edge) for edge in uedges):
                    tile = flip_y(tile)

            starty = y * (tile_height - 2)
            startx = x * (tile_width - 2)

            for dy in range(tile_height - 2):
                for dx in range(tile_width - 2):
                    canvas[starty + dy][startx + dx] = tile[dy + 1][dx + 1]

    return count_monsters(canvas)


def parse_input(data: Sequence[str]) -> Dict[int, List[str]]:
    tiles = {}
    tile = []
    tile_id = -1

    for line in data:
        if line.strip():
            if ints(line):
                tile_id = ints(line)[0]
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

    print(solve(tiles))  # Answer = 1957


if __name__ == '__main__':
    main()

"""
--- Day 17: Conway Cubes ---

As your flight slowly drifts through the sky, the Elves at the Mythical Information Bureau at the North Pole contact you
They'd like some help debugging a malfunctioning experimental energy source aboard one of their super-secret imaging
satellites.

The experimental energy source is based on cutting-edge technology: a set of Conway Cubes contained in a
pocket dimension! When you hear it's having problems, you can't help but agree to take a look.

The pocket dimension contains an infinite 3-dimensional grid. At every integer 3-dimensional coordinate (x,y,z),
there exists a single cube which is either active or inactive.

In the initial state of the pocket dimension, almost all cubes start inactive.
The only exception to this is a small flat region of cubes (your puzzle input); the cubes in this region start in the
specified active (#) or inactive (.) state.

The energy source then proceeds to boot up by executing six cycles.

Each cube only ever considers its neighbors:
any of the 26 other cubes where any of their coordinates differ by at most 1.
For example, given the cube at x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at x=0,y=2,z=3,
and so on.

During a cycle, all cubes simultaneously change their state according to the following rules:

   If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
   Otherwise, the cube becomes inactive.
   If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active.
   Otherwise, the cube remains inactive.

The engineers responsible for this experimental energy source would like you to simulate the pocket dimension and
determine what the configuration of cubes should be at the end of the six-cycle boot process.

For example, consider the following initial state:

.#.
..#
###

Even though the pocket dimension is 3-dimensional, this initial state represents a small 2-dimensional slice of it.
(In particular, this initial state defines a 3x3x1 region of the 3-dimensional space.)

Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle
is shown layer-by-layer at each given z coordinate (and the frame of view follows the active cells in each cycle):

Before any cycles:

z=0
.#.
..#
###


After 1 cycle:

z=-1
#..
..#
.#.

z=0
#.#
.##
.#.

z=1
#..
..#
.#.


After 2 cycles:

z=-2
.....
.....
..#..
.....
.....

z=-1
..#..
.#..#
....#
.#...
.....

z=0
##...
##...
#....
....#
.###.

z=1
..#..
.#..#
....#
.#...
.....

z=2
.....
.....
..#..
.....
.....


After 3 cycles:

z=-2
.......
.......
..##...
..###..
.......
.......
.......

z=-1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=0
...#...
.......
#......
.......
.....##
.##.#..
...#...

z=1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=2
.......
.......
..##...
..###..
.......
.......
.......

After the full six-cycle boot process completes, 112 cubes are left in the active state.

Starting with your given initial configuration, simulate six cycles.
How many cubes are left in the active state after the sixth cycle?

"""
from dataclasses import dataclass
from typing import Dict, Iterator, Set, Tuple

Coordinates = Tuple[int, int, int]


def iter_neighbors(x: int, y: int, z: int) -> Iterator[Coordinates]:
    for nx in [x - 1, x, x + 1]:
        for ny in [y - 1, y, y + 1]:
            for nz in [z - 1, z, z + 1]:
                if (nx, ny, nz) == (x, y, z):
                    continue

                yield nx, ny, nz


@dataclass
class PocketDimension:
    active_cubes: Set[Coordinates]

    def is_active(self, x: int, y: int, z: int) -> bool:
        return (x, y, z) in self.active_cubes

    def copy(self):
        return PocketDimension(self.active_cubes.copy())

    def step(self) -> 'PocketDimension':
        """
        Returns a copy of this pocket dimension evolved by 1 step.
        """
        new_active_cubes = set()
        # Maps each inactive which can be potentially activated to the number of active neighbors it has
        activation_candidates: Dict[Coordinates, int] = {}
        for x, y, z in self.active_cubes:
            neighbors_count = 0
            for nx, ny, nz in iter_neighbors(x, y, z):
                if self.is_active(nx, ny, nz):
                    neighbors_count += 1
                else:
                    activation_candidates.setdefault((nx, ny, nz), 0)
                    activation_candidates[(nx, ny, nz)] += 1

            if neighbors_count == 2 or neighbors_count == 3:
                new_active_cubes.add((x, y, z))

        for (x, y, z), neighbors_count in activation_candidates.items():
            if neighbors_count == 3:
                new_active_cubes.add((x, y, z))

        return PocketDimension(new_active_cubes)


def parse_pocket_dimensions(content: str) -> PocketDimension:
    content = content.strip()

    active_cubes = set()
    for line_ix, line in enumerate(content.split('\n')):
        line = line.strip()
        for char_ix, char in enumerate(line):
            if char == '.':
                continue
            elif char == '#':
                active_cubes.add((char_ix, line_ix, 0))

    return PocketDimension(active_cubes)


def main():
    with open('./input.txt') as f:
        puzzle_input = f.read()
        original_dimension = parse_pocket_dimensions(puzzle_input)

    cycles = 6

    dimension = original_dimension
    for _ in range(cycles):
        dimension = dimension.step()
    print(len(dimension.active_cubes))  # Answer = 284


if __name__ == "__main__":
    main()  # Original Solution by Oleg Yam

"""
--- Part Two ---

For some reason, your simulated results don't match what the experimental energy source engineers expected.
Apparently, the pocket dimension actually has four spatial dimensions, not three.

The pocket dimension contains an infinite 4-dimensional grid. At every integer 4-dimensional coordinate (x,y,z,w),
there exists a single cube (really, a hypercube) which is still either active or inactive.

Each cube only ever considers its neighbors: any of the 80 other cubes where any of their coordinates differ by at
most 1. For example, given the cube at x=1,y=2,z=3,w=4, its neighbors include the cube at x=2,y=2,z=3,w=3,
the cube at x=0,y=2,z=3,w=4, and so on.

The initial state of the pocket dimension still consists of a small flat region of cubes. Furthermore, the same rules
for cycle updating still apply: during each cycle, consider the number of active neighbors of each cube.

For example, consider the same initial state as in the example above. Even though the pocket dimension is
4-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state
defines a 3x3x1x1 region of the 4-dimensional space.)

Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle
is shown layer-by-layer at each given z and w coordinate:

Before any cycles:

z=0, w=0
.#.
..#
###


After 1 cycle:

z=-1, w=-1
#..
..#
.#.

z=0, w=-1
#..
..#
.#.

z=1, w=-1
#..
..#
.#.

z=-1, w=0
#..
..#
.#.

z=0, w=0
#.#
.##
.#.

z=1, w=0
#..
..#
.#.

z=-1, w=1
#..
..#
.#.

z=0, w=1
#..
..#
.#.

z=1, w=1
#..
..#
.#.


After 2 cycles:

z=-2, w=-2
.....
.....
..#..
.....
.....

z=-1, w=-2
.....
.....
.....
.....
.....

z=0, w=-2
###..
##.##
#...#
.#..#
.###.

z=1, w=-2
.....
.....
.....
.....
.....

z=2, w=-2
.....
.....
..#..
.....
.....

z=-2, w=-1
.....
.....
.....
.....
.....

z=-1, w=-1
.....
.....
.....
.....
.....

z=0, w=-1
.....
.....
.....
.....
.....

z=1, w=-1
.....
.....
.....
.....
.....

z=2, w=-1
.....
.....
.....
.....
.....

z=-2, w=0
###..
##.##
#...#
.#..#
.###.

z=-1, w=0
.....
.....
.....
.....
.....

z=0, w=0
.....
.....
.....
.....
.....

z=1, w=0
.....
.....
.....
.....
.....

z=2, w=0
###..
##.##
#...#
.#..#
.###.

z=-2, w=1
.....
.....
.....
.....
.....

z=-1, w=1
.....
.....
.....
.....
.....

z=0, w=1
.....
.....
.....
.....
.....

z=1, w=1
.....
.....
.....
.....
.....

z=2, w=1
.....
.....
.....
.....
.....

z=-2, w=2
.....
.....
..#..
.....
.....

z=-1, w=2
.....
.....
.....
.....
.....

z=0, w=2
###..
##.##
#...#
.#..#
.###.

z=1, w=2
.....
.....
.....
.....
.....

z=2, w=2
.....
.....
..#..
.....
.....

After the full six-cycle boot process completes, 848 cubes are left in the active state.

Starting with your given initial configuration, simulate six cycles in a 4-dimensional space. How many cubes are left
in the active state after the sixth cycle?

"""
from dataclasses import dataclass
from typing import Dict, Iterator, Set, Tuple

Coordinates = Tuple[int, int, int, int]


def iter_neighbors(x: int, y: int, z: int, w: int) -> Iterator[Coordinates]:
    for nx in [x - 1, x, x + 1]:
        for ny in [y - 1, y, y + 1]:
            for nz in [z - 1, z, z + 1]:
                for nw in [w - 1, w, w + 1]:
                    if (nx, ny, nz, nw) == (x, y, z, w):
                        continue

                    yield nx, ny, nz, nw


@dataclass
class PocketDimension:
    active_cubes: Set[Coordinates]

    def is_active(self, x: int, y: int, z: int, w: int) -> bool:
        return (x, y, z, w) in self.active_cubes

    def copy(self):
        return PocketDimension(self.active_cubes.copy())

    def step(self) -> 'PocketDimension':
        """
        Returns a copy of this pocket dimension evolved by 1 step.
        """
        new_active_cubes = set()
        # Maps each inactive which can be potentially activated to the number of active neighbors it has
        activation_candidates: Dict[Coordinates, int] = {}
        for x, y, z, w in self.active_cubes:
            neighbors_count = 0
            for nx, ny, nz, nw in iter_neighbors(x, y, z, w):
                if self.is_active(nx, ny, nz, nw):
                    neighbors_count += 1
                else:
                    activation_candidates.setdefault((nx, ny, nz, nw), 0)
                    activation_candidates[(nx, ny, nz, nw)] += 1

            if neighbors_count == 2 or neighbors_count == 3:
                new_active_cubes.add((x, y, z, w))

        for (x, y, z, w), neighbors_count in activation_candidates.items():
            if neighbors_count == 3:
                new_active_cubes.add((x, y, z, w))

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
                active_cubes.add((char_ix, line_ix, 0, 0))

    return PocketDimension(active_cubes)


def main():
    with open('./input.txt') as f:
        puzzle_input = f.read()
        original_dimension = parse_pocket_dimensions(puzzle_input)

    dimension = original_dimension
    cycles = 6

    for i in range(cycles):
        dimension = dimension.step()
    print(len(dimension.active_cubes))   # Answer = 2240


if __name__ == "__main__":
    main()  # Original solution by Oleg Yam

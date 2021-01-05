"""
--- Day 12: Rain Risk ---

Your ferry made decent progress toward the island, but the storm came in faster than anyone expected.
The ferry needs to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety,
it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help,
you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer
input values. After staring at them for a few minutes, you work out what they probably mean:

    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the direction the ship is currently facing.

The ship starts by facing east. Only the L and R actions change the direction the ship is facing.
(That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would
still move east if the following action were F.)

For example:

F10
N3
F7
R90
F11

These instructions would be handled as follows:

    F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
    N3 would move the ship 3 units north to east 10, north 3.
    F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
    R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
    F11 would move the ship 11 units south to east 17, south 8.

At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position
and its north/south position) from its starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's
starting position?

"""
from typing import Union, List, Tuple, Sequence


def move(_direction: str, amount: int, _location: Tuple[int, int]) -> Tuple[int, int]:
    """
    Updates the _location based on +x, -y positioning.
    """
    if _direction == "N":
        return _location[0], _location[1] + amount
    if _direction == "S":
        return _location[0], _location[1] - amount
    if _direction == "E":
        return _location[0] + amount, _location[1]
    if _direction == "W":
        return _location[0] - amount, _location[1]


def ship_movements(data: Sequence[str]) -> int:
    directions = [(d[:1], int(d[1:])) for d in data]
    facing = "E"
    origin = (0, 0)
    location = (0, 0)

    def turn(_direction: Tuple[str, int]) -> Union[str, List[str]]:
        """
        Jumps to the new direction based on the current facing direction + the direction degrees divided by 90.
        """
        options = ("E", "S", "W", "N", "E", "S", "W", "N")
        jumps = (_direction[1] // 90) if (_direction[0] == "R") else (- _direction[1] // 90)
        return options[options.index(facing) + jumps]

    for direction in directions:
        if (direction[0] == "R") or (direction[0] == "L"):
            facing = turn(direction)
        elif direction[0] == "F":  # "F" direction moves in the "facing" direction.
            location = move(facing, direction[1], location)
        else:
            location = move(direction[0], direction[1], location)

    return abs(origin[0] - location[0]) + abs(origin[1] - location[1])


def main():
    with open("./input.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print(ship_movements(puzzle_input))  # Answer = 521


if __name__ == '__main__':
    main()

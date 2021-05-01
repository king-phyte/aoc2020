"""
Before you leave, the Elves in accounting just need you to fix your expense
report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then
multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying
them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum
to 2020; what do you get if you multiply them together?

"""
from typing import Sequence, List, Tuple, Union
from functools import reduce


def find_target(numbers: Sequence[int], target: int) -> Union[Tuple[int, int], tuple]:
    """
    Returns 2 numbers in :param numbers such that the sum of the 2 numbers is equal to the target.
    Returns an empty tuple if the above criteria is not met
    >>> find_target([1721, 979, 366, 299, 675,1456], 2020)
    (1721, 299)
    """
    for number in numbers:
        remainder = target - number
        if remainder in numbers:
            return number, remainder
    return ()


def multiply(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Returns the result of multiplying 2 numbers
    """
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return x * y
    raise NotImplementedError("Both inputs must be of type (int, float)")


def main() -> None:
    with open("./input.txt") as f:
        numbers: List[int] = [int(line.strip()) for line in f.readlines()]

    print(reduce(multiply, find_target(numbers, target=2020)))   # Answer = 567171


if __name__ == '__main__':
    main()

"""
--- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers you
a starfish coin they had left over from a past vacation. They offer
you a second one if you can find three numbers in your expense
report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979,
366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries
that sum to 2020?
"""
from typing import Sequence, Tuple, Union
from part_1 import multiply
from functools import reduce


def find_target(numbers: Sequence[int], target: int) -> Union[Tuple[int, int, int], tuple]:
    """
    Returns 3 numbers in :param numbers such that their sum is equal to the target.
    >>> find_target([1721, 979, 366, 299, 675,1456], 2020)
    (675, 366, 979)
    >>> find_target([1721, 979, 366, 299, 675,1456], 2021)
    ()
    """
    numbers: Tuple[int] = tuple(set(numbers))
    index_of_first_number = 0

    for number in numbers:
        for second_number in numbers[index_of_first_number + 1:]:
            for third_number in numbers[index_of_first_number + 2:]:
                _sum = number + second_number + third_number
                if _sum == target:
                    return number, second_number, third_number
    return ()


def main() -> None:
    with open("./input.txt") as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    print(reduce(multiply, find_target(numbers, target=2020)))  # Answer = 212428694


if __name__ == '__main__':
    main()

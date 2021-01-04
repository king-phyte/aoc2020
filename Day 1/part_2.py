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
from typing import Sequence

TARGET = 2020


def find_target(numbers: Sequence[int]) -> int:

    index_of_second_number = 0
    index_of_third_number = 1

    for number in set(numbers):
        while index_of_second_number < len(numbers):
            while index_of_third_number < len(numbers):
                second_number = numbers[index_of_second_number]
                third_number = numbers[index_of_third_number]

                sum_ = number + second_number + third_number

                if sum_ == TARGET:
                    return (number * numbers[index_of_second_number]
                            * numbers[index_of_third_number])

                index_of_third_number += 1
            index_of_second_number += 1
            index_of_third_number = 1
        index_of_second_number = 0


def main():
    with open("./input.txt") as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    print(find_target(numbers))  # Answer = 212428694


if __name__ == '__main__':
    main()

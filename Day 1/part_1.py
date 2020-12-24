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

TARGET = 2020

with open("./day_one_input.txt") as f:
    numbers = []
    for line in f:
        numbers.append(int(line.strip()))


def find_target(numbers):
    # index_of_second_number = 1
    # for number in set(numbers):
    #     while index_of_second_number < len(numbers):
    #         second_number = numbers[index_of_second_number]
    #         if number + second_number == TARGET:
    #             return number * second_number
    #         index_of_second_number += 1
    #     index_of_second_number = 0

    for number in numbers:
        remainder = TARGET - number
        if remainder in numbers:
            return remainder * number


print(find_target(numbers))

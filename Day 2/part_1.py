"""
--- Day 2: Password Philosophy ---

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers;
we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the
Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords
(according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the lowest and
highest number of times a given letter must appear for the password to be valid.
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b,
but needs at least 1. The first and third passwords are valid:
they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

"""
from typing import Union


def is_valid(pwd: str, char: Union[str, int], minimum: int, maximum: int) -> bool:
    """
    The function checks whether a password is valid or not.
    The validation is such that, the password must contain the character to be validated at least a certain number
    of times but not more than a certain number of times.
    Hence, the character occurrence is such that: minimum <= character occurrence <= maximum
    If the above holds true, the function returns True. Else, it returns False.
    :param pwd: str - The password to be validated.
    :param char: Union[int, str] - The character to be used for validation.
    :param minimum: int - Minimum occurrence of the character to be validated.
    :param maximum: int - Maximum occurrence of the character to be validated.
    :return: bool
    """

    if char not in pwd:
        return False
    character_occurrence = pwd.count(char)
    if character_occurrence < minimum or character_occurrence > maximum:
        return False
    return True


def find_number_of_valid_passwords(data: list) -> int:
    number_of_valid_passwords = 0

    for line in data:
        line_content = line.split()
        min_and_max_occurrence = line_content[0].split("-")
        minimum_occurrence = int(min_and_max_occurrence[0])
        maximum_occurrence = int(min_and_max_occurrence[1])
        character_to_validate = line_content[1][:-1]
        password = line_content[2]

        if is_valid(password, character_to_validate, minimum_occurrence, maximum_occurrence):
            number_of_valid_passwords += 1

    return number_of_valid_passwords


def main():
    with open("./input.txt") as f:
        puzzle_input = f.readlines()

    find_number_of_valid_passwords(puzzle_input)


if __name__ == '__main__':
    print(main())  # Answer: 519

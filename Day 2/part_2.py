"""
--- Part Two ---

While it appears you validated the passwords correctly, they don't seem to be what the
Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job
at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character,
2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant
for the purposes of policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?

"""
from typing import Union, Sequence


def is_valid(pwd: str, char: Union[str, int], first_position: int, last_position: int) -> bool:
    """
    The function checks whether a password is valid or not.
    The validation is such that, the password must contain the character to be validated at least a certain number
    of times but not more than a certain number of times.
    Hence, the character occurrence is such that: minimum <= character occurrence <= maximum
    If the above holds true, the function returns True. Else, it returns False.

    :param pwd: str - The password to be validated.
    :param char: Union[int, str] - The character to be used for validation.
    :param first_position: int - Minimum occurrence of the character to be validated.
    :param last_position: int - Maximum occurrence of the character to be validated.
    :return: bool
    """

    if char not in pwd:
        return False
    if (char == pwd[first_position - 1]) and (char != pwd[last_position - 1]):
        return True
    elif (char != pwd[first_position - 1]) and (char == pwd[last_position - 1]):
        return True
    else:
        return False


def find_number_of_valid_passwords(data: Sequence[str]) -> int:
    """
    Finds the number of valid passwords in the data argument.
    It takes all elements in the data and checks their validity with the is_valid function.
    The function return the total number of valid passwords found.

    :param data:
    :return:
    """
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

    print(find_number_of_valid_passwords(puzzle_input))  # Answer: 708


if __name__ == '__main__':
    main()

"""
--- Part Two ---

The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data
are getting through. Better add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for
automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both present and valid according to the above rules.
Here are some example values:

byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789

Here are some invalid passports:

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

Here are some valid passports:

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719

Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as
optional. In your batch file, how many passports are valid?

"""

from typing import List
from part_1 import group_passport_data


def birth_year_is_valid(year: int) -> bool:
    """
    Checks if a birth year is valid.
    A birth year is valid if it is such that: 1920 <= year <= 2002.
    Examples:
        - Valid: 1920, 2002, 1995
        - Invalid: 1919 (less than 1920), 2003 (greater than 2002)
    The function returns True if it is valid. Otherwise, it returns False.

    :param year: int - Year to be validated
    :return: bool
    """
    return True if (1920 <= year <= 2002) else False


def expiration_year_is_valid(year: int) -> bool:
    """
     Checks if a passport's expiration year is valid.
     The expiration year is valid if it is such that: 2020 <= year <= 2030.
     Examples:
        - Valid: 2020, 2030, 2026
        - Invalid: 2019 (less than 2020), 2031 (greater than 2030)
     The function returns True if it is valid. Otherwise, it returns False.

     :param year: int - Year to be validated
     :return: bool
     """
    return True if (2020 <= year <= 2030) else False


def issue_year_is_valid(year: int) -> bool:
    """
     Checks if a passport's year of issue is valid.
     The year of issue is valid if it is such that: 2010 <= year <= 2020.
     Examples:
        - Valid: 2010, 2018, 2020
        - Invalid: 2009 (less than 2010), 2021 (greater than 2020)
     The function returns True if it is valid. Otherwise, it returns False.

     :param year: int - Year to be validated
     :return: bool
     """
    return True if (2010 <= year <= 2020) else False


def height_is_valid(height: str) -> bool:
    """
    Checks if a person's height is valid.
    For a person's height to be valid, it must satisfy the following:
        - It must be a number followed by either cm or in:
        - If cm, the number must be at least 150 and at most 193.
        - If in, the number must be at least 59 and at most 76.
    Examples:
        - Valid: 150cm, 76in
        - Invalid: 150 (No unit), 77in ("in" must not be greater than 76)
    The function returns True if the height is valid and False if it is not.

    :param height: int - Height to be validated
    :return: bool
    """
    height_unit = height[-2:]

    if (height_unit != "cm") and (height_unit != "in"):
        return False

    if height_unit == "cm":
        return True if (150 <= int(height[:-2]) <= 193) else False

    elif height_unit == "in":
        return True if (59 <= int(height[:-2]) <= 76) else False


def eye_color_is_valid(color: str) -> bool:
    """
    Checks if a person's eye color is valid.
    For a person's eye color to be valid, it must have exactly one of "amb", "blu", "brn", "gry", "grn", "hzl" or "oth".
    The function returns True if the eye color is valid and False if it is not.

    :param color: str - Color to be validated
    :return: bool
    """
    colors = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    return True if (color in colors) else False


def hair_color_is_valid(hexadecimal_color: str) -> bool:
    """
    Checks if a Hexadecimal RGB is valid or not.
    For the color to be valid, it must begin with a # followed by exactly six characters 0-9 or a-f.
    Examples:
        - Valid: #1ef014, #000000, #aaaaaa
        - Invalid: 123410 (No #), #31 (less than 6 chars after #), #12r32c (r is not within a-f)
    The function returns True if the color is valid and False if it is not.

    :param hexadecimal_color: str - Hexadecimal color
    :return: bool
    """
    valid_characters: List[str] = [str(i) for i in range(10)]
    valid_characters += ["a", "b", "c", "d", "e", "f"]

    if not hexadecimal_color.startswith("#") and (len(hexadecimal_color) <= 7):
        return False

    for character in hexadecimal_color[1:]:
        if character not in valid_characters:
            return False
    return True


def passport_id_is_valid(passport_id: str) -> bool:
    """
    Checks if a passport ID is valid.
    The ID is valid if it's length is 9
    The function return True if the ID is valid else it returns False.

    :param passport_id: str - The Passport ID to be validated.
    :return: bool
    """
    return True if (len(passport_id) == 9) else False


def passport_is_valid(passport: dict) -> bool:
    """
    Checks whether a passport is valid or not.
    A passport is considered valid if all the functions called by this function returns True.
    If a required field is not found in the passport and it raises a KeyError, the passport is considered invalid.
    If a passport is valid, the function returns True. Otherwise, it returns False.

    :param passport: dict
    :return: bool
    """
    try:
        birth_year = int(passport["byr"])
        issue_year = int(passport["iyr"])
        expiration_year = int(passport["eyr"])
        height = passport["hgt"]
        hair_color = passport["hcl"]
        eye_color = passport["ecl"]
        passport_id = passport["pid"]
    except KeyError:
        return False

    if birth_year_is_valid(birth_year) \
            and issue_year_is_valid(issue_year) \
            and expiration_year_is_valid(expiration_year) \
            and height_is_valid(height) \
            and eye_color_is_valid(eye_color) \
            and hair_color_is_valid(hair_color) \
            and passport_id_is_valid(passport_id):
        return True
    return False


def main():
    with open("./input.txt") as f:
        content: List[str] = [line.strip() for line in f.readlines()]
    passports: List[dict] = []
    number_of_valid_passports = 0

    # Use newlines ("") to find sections of info belonging to a passport
    while "" in content:
        index = content.index("")
        passports.append(group_passport_data(content[:index]))
        content = content[index + 1:]  # Remove the contents which has been grouped
    else:
        passports.append(group_passport_data(content))  # Take care of the last section of info left which has no ""

    for passport_info in passports:
        if passport_is_valid(passport_info):
            number_of_valid_passports += 1

    print(number_of_valid_passports)  # Answer = 137


if __name__ == '__main__':
    main()

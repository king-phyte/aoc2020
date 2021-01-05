"""
--- Day 4: Passport Processing ---

You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport.
While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore
aren't actually valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport
scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these problems
at the same time.

The automatic passport scanners are slow because they're having trouble detecting which passports have
all required fields. The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence
of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in

The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt
(the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials,
not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields.
Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not,
so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional.
In your batch file, how many passports are valid?

"""
from typing import List, Sequence, Dict


def group_passport_data(data: Sequence[str]) -> Dict[str, str]:
    """
    Groups a list of string values into a dictionary.
    It splits the data by spaces and a colon(:) and generates a key-value pair.
    Returns a dictionary of passport information.

    :param data: list - Data to be added to the dictionary.
    :return: dict - A dictionary of passport info.
    """
    passport = {}

    for string in data:
        for group in string.split():
            item = group.split(":")
            property_ = item[0]
            value = item[1]
            passport[property_] = value

    return passport


def passport_is_valid(passport:  Dict[str, str]) -> bool:
    """
    Checks if a passport is valid or not.
    A passport is valid if it has all of the following keys:
    "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
    A passport can also have a "cid" key but it is not a requirement for a passport to be valid.
    The function returns True if a password is valid and False if it is not.

    :param passport: dict - Information about a passport
    :return: bool
    """
    passport_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid")

    required = passport_fields[:-1]  # cid is optional (not required).

    for field in required:
        if field not in passport.keys():
            return False
    return True


def main():
    with open("./input.txt") as f:
        content: List[str] = [line.strip() for line in f.readlines()]

    passports = []

    while "" in content:
        index = content.index("")
        passports.append(group_passport_data(content[:index]))
        content = content[index + 1:]
    else:
        passports.append(group_passport_data(content))

    number_of_valid_passports = 0

    for passport_info in passports:
        if passport_is_valid(passport_info):
            number_of_valid_passports += 1

    print(number_of_valid_passports)  # Answer = 202


if __name__ == '__main__':
    main()

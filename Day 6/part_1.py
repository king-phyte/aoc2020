"""
--- Day 6: Custom Customs ---

As your flight approaches the regional airport where you'll switch to a much larger plane,
customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions
for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help.
For each of the people in their group, you write down the questions for which they answer "yes", one per line.

For example:

abcx
abcy
abcz

In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z.
(Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane
(your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers
are on a single line. For example:

abc

a
b
c

ab
ac

a
a
a
a

b

This list represents answers from five groups:

    The first group contains one person who answered "yes" to 3 questions: a, b, and c.
    The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
    The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
    The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
    The last group contains one person who answered "yes" to only 1 question, b.

In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

"""
from typing import List, Sequence


def number_of_yes_in_group(group: Sequence[str]) -> int:
    """
    Finds the number of yeses in a group.
    Since duplicate yeses are not counted, they are removed with "set()" function
    The number of yeses corresponds to the size of the group without duplicates.
    The function returns the number of yeses as described above.

    :param group: Sequence[str] - Answers from a group
    :return: int - Number of yeses in a group
    """
    return len(set(group))


def make_input_convenient(raw_input: Sequence[str]) -> List[str]:
    """
    Makes an input convenient for further processing.
    This is done by flattening out the list.
    The function returns a list of strings convenient for processing.


    :param raw_input: List[str] - A list of strings to be made convenient.
    :return: - List[str] - Convenient output
    """
    convenient = []

    for lst in raw_input:
        for char in lst:
            convenient.append(char)

    return convenient


def main():
    with open("./input.txt") as f:
        puzzle_input = [i.strip() for i in f.readlines()]

    groups: List[list] = []

    while "" in puzzle_input:
        index = puzzle_input.index("")
        groups.append(make_input_convenient(puzzle_input[:index]))
        puzzle_input = puzzle_input[index + 1:]
    else:
        groups.append(make_input_convenient(puzzle_input))

    total_number_of_yeses = 0

    for group in groups:
        total_number_of_yeses += number_of_yes_in_group(group)

    print(total_number_of_yeses)  # Answer = 6297


if __name__ == '__main__':
    main()

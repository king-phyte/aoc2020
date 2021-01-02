"""
--- Part Two ---

As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes";
you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

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

    In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
    In the second group, there is no question to which everyone answered "yes".
    In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c,
    they don't count.
    In the fourth group, everyone answered yes to only 1 question, a.
    In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.

In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

"""
from typing import List


def restart_search(chars, group_size, yes):
    for char in chars:
        if chars.count(char) == group_size:
            yes += 1
            while char in chars:
                chars.pop(chars.index(char))
        else:
            while char in chars:
                chars.pop(chars.index(char))

    return chars, yes


def number_of_yes_in_group(group: List[str]) -> int:
    """
    Finds and returns the number of yeses in a group.
    :param group:
    :return:
    """
    group_size = len(group)
    if group_size == 1:
        return len(group[0])

    yeses = 0

    chars = []
    for string in group:
        for char in string:
            chars.append(char)

    while len(chars) > 0:
        c, y = restart_search(chars, group_size, yeses)
        chars = c
        yeses = y

    return yeses


def make_input_convenient(raw_input: List[str]) -> List[str]:
    """
    Makes an input convenient for further processing.
    This is done by flattening out the list.
    The function returns a list of strings convenient for processing.


    :param raw_input: List[str] - A list of strings to be made convenient.
    :return: - List[str] - Convenient output
    """
    convenient = []

    for lst in raw_input:
        convenient.append(lst)

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

    print(total_number_of_yeses)  # Answer = 3158


if __name__ == '__main__':
    main()

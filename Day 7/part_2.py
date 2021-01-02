"""
--- Part Two ---

It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of
bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

    faded blue bags contain 0 other bags.
    dotted black bags contain 0 other bags.
    vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
    dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags
(and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example;
be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?

"""

from typing import Dict, Union

with open("./input.txt") as f:
    puzzle_input = [line.strip() for line in f.readlines()]


def bags_in(desired_bag: str) -> Union[Dict[str, int], dict]:
    """
    Finds all the bags in a desired bag.
    Returns a dictionary of {bag_name : number_of_bags_it_can_contain}.
    If the desired bag does not contain any bag, it returns an empty dictionary.
    :param desired_bag: str - The bags inside this bag will be found.
    :return: Union[Dict[str, int], dict] - All bags inside the desired bag.
    """
    bags = {}
    for line in puzzle_input:
        if line.startswith(desired_bag) and ("no other" in line):
            return {}
        if line.startswith(desired_bag):
            contain_end_index = line.index(" contain ") + len(" contain ")
            content = line[contain_end_index:-1]  # -1 to remove trailing .
            content = content.split(", ")
            for bag in content:
                can_contain = int(bag[0])
                bag = bag[2: bag.index(" bag")]
                bags[bag] = can_contain
    return bags
            
            
def count_bags_inside(bag: str) -> int:
    """
    Recursively counts the number of bags inside a bag.

    :param bag: str - The  bag to be whose contents should be counted.
    :return: int - The total number of bags inside the bag.
    """

    bags = bags_in(bag)
    count = 0
    if bags == {}:
        return 0
    for bag in bags:
        count += bags[bag]
        count += bags[bag] * count_bags_inside(bag)
    return count


def main():
    my_bag = "shiny gold"
    print(count_bags_inside(my_bag))  # Answer = 176035


if __name__ == '__main__':
    main()

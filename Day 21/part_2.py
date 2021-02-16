"""
--- Part Two ---

Now that you've isolated the inert ingredients, you should have enough information to figure out which ingredient
contains which allergen.

In the above example:

    mxmxvkd contains dairy.
    sqjhc contains fish.
    fvjkl contains soy.

Arrange the ingredients alphabetically by their allergen and separate them by commas to produce your canonical
dangerous ingredient list. (There should not be any spaces in your canonical dangerous ingredient list.)
In the above example, this would be mxmxvkd,sqjhc,fvjkl.

Time to stock your raft with supplies. What is your canonical dangerous ingredient list?

"""
from typing import Dict, Set
from part_1 import parse_input, find_allergens


def find_dangerous_ingredients(allergens: Dict[Set[str], Set[str]]) -> str:
    return ','.join(list(pair[1])[0] for pair in sorted((k, v) for k, v in allergens.items()))


def main():
    with open("./input.txt") as f:
        puzzle_input = f.readlines()

    lines = parse_input(puzzle_input)
    allergens = find_allergens(lines)

    print(find_dangerous_ingredients(allergens))  # Answer = xncgqbcp,frkmp,qhqs,qnhjhn,dhsnxr,rzrktx,ntflq,lgnhmx


if __name__ == '__main__':
    main()

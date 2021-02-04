"""
--- Day 21: Allergen Assessment ---

You reach the train's last stop and the closest you can get to your vacation island without getting wet.
There aren't even any boats here, but nothing can stop you now: you build a raft.
You just need a few days' worth of food for your journey.

You don't speak the local language, so you can't read any ingredients lists.
However, sometimes, allergens are listed in a language you do understand.
You should be able to use this information to determine which ingredient contains which allergen
and work out which foods are safe to take with you on your trip.

You start by compiling a list of foods (your puzzle input), one food per line.
Each l5ine includes that food's ingredients list followed by some or all of the allergens the food contains.

Each allergen is found in exactly one ingredient.
Each ingredient contains zero or one allergen.
Allergens aren't always marked; when they're listed (as in (contains nuts, shellfish) after an ingredients list),
the ingredient that contains each listed allergen will be somewhere in the corresponding ingredients list.
However, even if an allergen isn't listed, the ingredient that contains that allergen could still be present:
maybe they forgot to label it, or maybe it was labeled in a language you don't know.

For example, consider the following list of foods:

mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)

The first food in the list has four ingredients (written in a language you don't understand):
mxmxvkd, kfcds, sqjhc, and nhms.
While the food might contain other allergens, a few allergens the food definitely contains are listed afterward:
dairy and fish.

The first step is to determine which ingredients can't possibly contain any of the allergens in any food in your list.
In the above example, none of the ingredients kfcds, nhms, sbzzf, or trh can contain an allergen.
Counting the number of times any of these ingredients appear in any ingredients list produces 5:
they all appear once each except sbzzf, which appears twice.

Determine which ingredients cannot possibly contain any of the allergens in your list.
How many times do any of those ingredients appear?

"""
from typing import List, Sequence, Tuple, Set, Dict
from functools import reduce


def ingredients_without_allergens(allergens, lines) -> int:
    used = set()

    for allergen in allergens.values():
        used |= allergen

    count = 0

    for ingredients, _ in lines:
        for ingredient in ingredients:
            if ingredient not in used:
                count += 1

    return count


def find_allergens(lines: Sequence[Tuple[Set[str], Set[str]]]) -> Dict[Set[str], Set[str]]:
    ingredients = [line[0] for line in lines]
    allergens = [line[1] for line in lines]
    ingredients = reduce(lambda a, b: a | b, ingredients)
    allergens = {allergen: set(ingredients) for allergen in reduce(lambda a, b: a | b, allergens)}

    for ingredient, _allergens in lines:
        for allergen in _allergens:
            allergens[allergen] &= ingredient

    definite = set()

    for ingredient in allergens.values():
        if len(ingredient) == 1:
            definite |= ingredient

    while True:
        reduct_dict = {}

        for key, ingredient in allergens.items():
            if len(ingredient - definite) == 1:
                reduct_dict[key] = ingredient - definite

        if not reduct_dict:
            break

        for k, v in reduct_dict.items():
            allergens[k] = v
            definite |= v

    return allergens


def parse_input(data: Sequence[str]) -> List[Tuple[Set[str], Set[str]]]:
    parsed_input = []

    for line in data:
        a, b = line.strip().split(" (contains ")
        ingredients = set(a.split())
        allergens = set([word[:-1] for word in b.split()])
        parsed_input.append((ingredients, allergens))

    return parsed_input


def main():
    with open('./input.txt') as f:
        puzzle_input = f.readlines()

    lines = parse_input(puzzle_input)
    allergens = find_allergens(lines)
    print(ingredients_without_allergens(allergens, lines))  # Answer = 2635


if __name__ == '__main__':
    main()

"""--- Part Two ---

Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner
and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together,
these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""
from part_1 import encountered_tree


def main():
    with open("./input.txt") as f:
        puzzle_input = f.readlines()

    # Duplicate the lines side by side 78 times to improve the convenience of transversing the lines.
    # There is no specific reason for choosing 78. It just was convenient at the time.
    # To stay safe, use multiple of 13 greater than or equal to 78
    convenient_input = [line.strip() * (13 * 6) for line in puzzle_input]

    product = 1
    product *= encountered_tree(convenient_input, 1, 1)
    product *= encountered_tree(convenient_input, 3, 1)
    product *= encountered_tree(convenient_input, 5, 1)
    product *= encountered_tree(convenient_input, 7, 1)
    product *= encountered_tree(convenient_input, 1, 2)
    print(product)  # Answer = 4385176320


if __name__ == "__main__":
    main()

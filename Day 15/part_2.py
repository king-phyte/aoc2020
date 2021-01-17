"""
--- Part Two ---

Impressed, the Elves issue you a challenge: determine the 30000000th number spoken.
For example, given the same starting numbers as above:

    Given 0,3,6, the 30000000th number spoken is 175594.
    Given 1,3,2, the 30000000th number spoken is 2578.
    Given 2,1,3, the 30000000th number spoken is 3544142.
    Given 1,2,3, the 30000000th number spoken is 261214.
    Given 2,3,1, the 30000000th number spoken is 6895259.
    Given 3,2,1, the 30000000th number spoken is 18.
    Given 3,1,2, the 30000000th number spoken is 362.

Given your starting numbers, what will be the 30000000th number spoken?

"""

from part_1 import play_numbers_game


def main():
    starting_numbers = [15, 5, 1, 4, 7, 0]
    print(play_numbers_game(starting_numbers, 30_000_000))  # Answer = 689


if __name__ == "__main__":
    main()

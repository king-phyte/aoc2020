"""
--- Part Two ---

The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous
set of at least two numbers in your list which sum to the invalid number from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576

In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course,
the contiguous set of numbers in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example,
these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?

"""
import part_1


def main():
    with open("./input.txt") as f:
        puzzle_input = [int(line.strip()) for line in f.readlines()]

    target = part_1.main()

    contiguous_set = []

    from_line = 0
    for _ in range(1000):
        for i in range(from_line, len(puzzle_input)):
            contiguous_set.append(puzzle_input[i])
            if sum(contiguous_set) == target:
                return min(contiguous_set), max(contiguous_set)
        from_line += 1
        contiguous_set = []


if __name__ == '__main__':
    min_, max_ = main()
    print(min_ + max_)  # Answer = 219202240

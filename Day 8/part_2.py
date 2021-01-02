"""
--- Part Two ---

After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp.
(No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in
the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6

If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop,
never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually
find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions
are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6

After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last
instruction in the file. With this change, after the program terminates, the accumulator contains the value 8
(acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp).
What is the value of the accumulator after the program terminates?

"""
from typing import List, Sequence, Optional, Tuple
import copy


def find_correct_loop(instructions_set:  List[Tuple[str, ...]]) -> Optional[int]:
    """
    Checks the index of the instruction to the length of the entire instruction list.
    # If the index is greater than or equal to the length of the instruction list, return the accumulator.
    :param instructions_set: List[Tuple[str, ...]] - A list of tuples of the instructions in the puzzle input.
    :return: Optional[int] - Accumulator.
    """
    length_of_instruction_set = len(instructions_set)
    accumulator = 0
    visited_indices = [0]
    while True:
        index = visited_indices[-1]
        instruction = instructions_set[index]

        if instruction[0] == 'jmp':
            index = index + int(instruction[1])

        if instruction[0] == 'acc':
            accumulator += int(instruction[1])
            index += 1

        if instruction[0] == 'nop':
            index += 1

        if index in visited_indices:
            return
        # Break if the index >= the total length of the instruction list and return the accumulated value.
        if index >= length_of_instruction_set:
            return accumulator

        visited_indices.append(index)


def fix_infinite_loop(puzzle_input: Sequence[str]) -> Optional[int]:
    """
    Changes instances of "jmp" and "nop" and runs to see which one runs the whole set of instructions without repeating.
    The function returns the accumulator if the code runs without infinite loop.
    :param puzzle_input: Sequence[str] - The puzzle input.
    :return: Optional[int] - The accumulator.
    """
    instruction_set = [tuple(i.split(" ")) for i in puzzle_input]

    for i in range(0, len(puzzle_input)):
        # Making a shallow copy of the instruction_set.
        copy_of_instructions = copy.copy(instruction_set)
        signed_integer = copy_of_instructions[i][1]

        if copy_of_instructions[i][0] == 'jmp':
            copy_of_instructions[i] = ('nop', signed_integer)

        elif copy_of_instructions[i][0] == 'nop':
            copy_of_instructions[i] = ('jmp', signed_integer)

        accumulator = find_correct_loop(copy_of_instructions)

        if accumulator:
            return accumulator


def main():

    with open("./input.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print(fix_infinite_loop(puzzle_input))  # Answer = 2060


if __name__ == '__main__':
    main()

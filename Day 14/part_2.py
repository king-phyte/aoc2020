"""
--- Part Two ---

For some reason, the sea port's computer system still can't communicate with your ferry's docking program.
It must be using version 2 of the decoder chip!

A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a memory address decoder.
Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the
destination memory address in the following way:

    If the bitmask bit is 0, the corresponding memory address bit is unchanged.
    If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
    If the bitmask bit is X, the corresponding memory address bit is floating.

A floating bit is not connected to anything and instead fluctuates unpredictably. In practice, this means the floating
bits will take on all possible values, potentially causing many memory addresses to be written all at once!

For example, consider the following program:

mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1

When this program goes to write to memory address 42, it first applies the bitmask:

address: 000000000000000000000000000000101010  (decimal 42)
mask:    000000000000000000000000000000X1001X
result:  000000000000000000000000000000X1101X

After applying the mask, four bits are overwritten, three of which are different, and two of which are floating.
Floating bits take on every possible combination of values; with two floating bits, four actual memory
addresses are written:

000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)
000000000000000000000000000000111010  (decimal 58)
000000000000000000000000000000111011  (decimal 59)

Next, the program is about to write to memory address 26 with a different bitmask:

address: 000000000000000000000000000000011010  (decimal 26)
mask:    00000000000000000000000000000000X0XX
result:  00000000000000000000000000000001X0XX

This results in an address with three floating bits, causing writes to eight memory addresses:

000000000000000000000000000000010000  (decimal 16)
000000000000000000000000000000010001  (decimal 17)
000000000000000000000000000000010010  (decimal 18)
000000000000000000000000000000010011  (decimal 19)
000000000000000000000000000000011000  (decimal 24)
000000000000000000000000000000011001  (decimal 25)
000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)

The entire 36-bit address space still begins initialized to the value 0 at every address, and you still need the sum of
all values left in memory at the end of the program. In this example, the sum is 208.

Execute the initialization program using an emulator for a version 2 decoder chip. What is the sum of all values left
in memory after it completes?

"""
from collections import defaultdict
import itertools
from typing import List

from part_1 import parse_instruction_set, binary_to_decimal

memory_block = defaultdict(int)


def flip_bits(address: str) -> List[str]:
    """
    Finds a list of all addresses in an address after it is masked.
    Returns a list of all addresses in binary (base 2)
    :param address: 36-bit memory address. Eg: 0000011011111X1001101X1011X1001111X1 - str
    :return: List of all addresses in the input address after masking - List[str]
    """
    all_addresses = []
    address = list(address)

    indices = [i for i, element in enumerate(address) if element == "X"]
    combinations = itertools.product(["0", "1"], repeat=len(indices))

    for items in combinations:
        for index, item in zip(indices, items):
            address[index] = item
        all_addresses.append("".join(address))
        return all_addresses


def execute_instructions(instruction_set: List[str]) -> None:
    mask = instruction_set[0].split("= ")[1]
    instructions = instruction_set[1:]

    for instruction in instructions:
        memory_address, value = instruction.split(" = ")
        memory_address = memory_address[4:-1]
        binary_memory_address = bin(int(memory_address))[2:]
        full_binary_memory_address = ("0" * (len(mask) - len(binary_memory_address))) + binary_memory_address

        new_binary_address = ""

        for b, m in zip(full_binary_memory_address, mask):
            if m == "0":
                new_binary_address += b
            elif m == "1":
                new_binary_address += m
            elif m == "X":
                new_binary_address += m

        addresses = flip_bits(new_binary_address)
        for address in addresses:
            memory_block[address] = int(value)


def main():
    with open("./input.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    convenient_input = parse_instruction_set(puzzle_input)
    for group in convenient_input:
        execute_instructions(group)

    print(sum(memory_block.values()))  # Answer = 3817372618036


if __name__ == '__main__':
    main()

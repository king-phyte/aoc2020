"""
--- Day 13: Shuttle Search ---

Your ferry can make it safely to a nearby port, but it won't get much further. When you call to book another ship,
you discover that no ships embark from that port to your vacation island.
You'll need to get from the port to the nearest airport.

Fortunately, a shuttle bus service is available to bring you from the sea port to the airport!
Each bus has an ID number that also indicates how often the bus leaves for the airport.

Bus schedules are defined based on a timestamp that measures the number of minutes since some fixed reference point in
the past. At timestamp 0, every bus simultaneously departed from the sea port.
After that, each bus travels to the airport, then various other locations, and finally returns to the sea port to
repeat its journey forever.

The time this loop takes a particular bus is also its ID number: the bus with ID 5 departs from the sea port at
timestamps 0, 5, 10, 15, and so on. The bus with ID 11 departs at 0, 11, 22, 33, and so on.
If you are there when the bus departs, you can ride that bus to the airport!

Your notes (your puzzle input) consist of two lines. The first line is your estimate of the earliest timestamp you
could depart on a bus. The second line lists the bus IDs that are in service according to the shuttle company;
entries that show x must be out of service, so you decide to ignore them.

To save time once you arrive, your goal is to figure out the earliest bus you can take to the airport.
(There will be exactly one such bus.)

For example, suppose you have the following notes:

939
7,13,x,x,59,x,31,19

Here, the earliest timestamp you could depart is 939, and the bus IDs in service are 7, 13, 59, 31, and 19.
Near timestamp 939, these bus IDs depart at the times marked D:

time   bus 7   bus 13  bus 59  bus 31  bus 19
929      .       .       .       .       .
930      .       .       .       D       .
931      D       .       .       .       D
932      .       .       .       .       .
933      .       .       .       .       .
934      .       .       .       .       .
935      .       .       .       .       .
936      .       D       .       .       .
937      .       .       .       .       .
938      D       .       .       .       .
939      .       .       .       .       .
940      .       .       .       .       .
941      .       .       .       .       .
942      .       .       .       .       .
943      .       .       .       .       .
944      .       .       D       .       .
945      D       .       .       .       .
946      .       .       .       .       .
947      .       .       .       .       .
948      .       .       .       .       .
949      .       D       .       .       .

The earliest bus you could take is bus ID 59. It doesn't depart until timestamp 944,
so you would need to wait 944 - 939 = 5 minutes before it departs.
Multiplying the bus ID by the number of minutes you'd need to wait gives 295.

What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait
for that bus?

"""
from typing import List


def find_soonest_bus(data: List[str]) -> int:
    """
    The soonest bus is the one greater than but closest to the timestamp.
    Multiply each bus number by the ceiling division of the timestamp and bus.
    Find the bus by the index of the smallest time.
    Find the wait time my subtracting the timestamp from the smallest time.
    Return the product of the bus number and the wait time.
    """
    timestamp = int(data[0].strip())
    buses = [int(x) for x in data[1].split(",") if x.isdecimal()]
    times = [bus * (-(timestamp // -bus)) for bus in buses]
    min_time = min(times)
    bus = buses[times.index(min_time)]
    wait_time = min_time - timestamp
    return bus * wait_time


def main():
    with open("./input.txt") as f:
        puzzle_input = f.readlines()

    print(find_soonest_bus(puzzle_input))  # Answer = 3269


if __name__ == '__main__':
    main()

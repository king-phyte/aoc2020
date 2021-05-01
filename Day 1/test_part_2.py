import pytest
from functools import reduce
from part_1 import multiply
from part_2 import find_target


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        (
            ([1721, 979, 366, 299, 675, 1456], 2020), (675, 366, 979)
        ),
        (
            ([1721, 979, 366, 299, 675, 1456], 2021), ()
        )
    ]
)
def test_correct_answer(test_input, expected_output):
    numbers, target = test_input
    assert find_target(numbers, target) == expected_output


def test_find_target():
    numbers = [1721, 979, 366, 299, 675, 1456]
    target = 2020
    assert reduce(multiply, find_target(numbers, target)) == 241861950

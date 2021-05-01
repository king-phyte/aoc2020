import pytest
from part_1 import find_target, multiply
from functools import reduce


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-3, 5.2) == pytest.approx(-15.6)
    assert multiply(2.1, 0.2) == pytest.approx(0.42)


@pytest.mark.parametrize(
    "test_input, result",
    [
        (
                ([1721, 979, 366, 299, 675, 1456], 2020), (1721, 299)
        ),
        (
                ([1721, 979, 366, 299, 675, 1456], 2021), ()
        )
    ]
)
def test_find_target(test_input, result):
    numbers, target = test_input
    assert find_target(numbers, target) == result


def test_correct_answer():
    numbers = [1721, 979, 366, 299, 675, 1456]
    target = 2020
    assert reduce(multiply, find_target(numbers, target=target)) == 514579

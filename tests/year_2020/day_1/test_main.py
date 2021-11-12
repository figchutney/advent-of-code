from puzzles.year_2020.day_1 import main

from .data import DUMMY_EXPENSE_REPORT


def test_multiply_2_values_that_sum_to_2020() -> None:
    actual = main.multiply_2_values_that_sum_to_2020(
        values=DUMMY_EXPENSE_REPORT
    )
    expected = 514579
    assert actual == expected


def test_multiply_3_values_that_sum_to_2020() -> None:
    actual = main.multiply_3_values_that_sum_to_2020(
        values=DUMMY_EXPENSE_REPORT
    )
    expected = 241861950
    assert actual == expected

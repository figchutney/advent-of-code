from puzzles.year_2020.day_1 import main

from .data import DUMMY_EXPENSE_REPORT


def test_get_2_values_that_sum_to_2020() -> None:
    actual = main.get_2_values_that_sum_to_2020(values=DUMMY_EXPENSE_REPORT)
    expected = (1721, 299)
    assert actual == expected


def test_main() -> None:
    actual = main.main(expense_report=DUMMY_EXPENSE_REPORT)
    expected = 514579
    assert actual == expected

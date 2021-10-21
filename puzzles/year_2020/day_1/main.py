from typing import List, Tuple

from .data import EXPENSE_REPORT


def get_2_values_that_sum_to_2020(values: List[int]) -> Tuple[int, int]:
    for value_1 in values:
        for value_2 in values:
            if value_1 + value_2 == 2020:
                return (value_1, value_2)
    raise ValueError("Uh oh! None of the values sum to 2020 :'(")


def main(expense_report: List[int] = EXPENSE_REPORT) -> int:
    expense_1, expense_2 = get_2_values_that_sum_to_2020(values=expense_report)
    return expense_1 * expense_2


if __name__ == "__main__":
    print(main())

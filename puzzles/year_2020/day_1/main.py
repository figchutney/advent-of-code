from typing import List

from .data import EXPENSE_REPORT

# PART 1


def multiply_2_values_that_sum_to_2020(
    values: List[int],
) -> int:
    for value_1 in values:
        for value_2 in values:
            if value_1 + value_2 == 2020:
                return value_1 * value_2
    raise ValueError("Uh oh! No two values sum to 2020 :'(")


# PART 2


def multiply_3_values_that_sum_to_2020(
    values: List[int],
) -> int:
    for value_1 in values:
        for value_2 in values:
            for value_3 in values:
                if value_1 + value_2 + value_3 == 2020:
                    return value_1 * value_2 * value_3
    raise ValueError("Uh oh! No three values sum to 2020 :'(")


if __name__ == "__main__":
    print(
        f"Part 1 Answer: "
        f"{multiply_2_values_that_sum_to_2020(values=EXPENSE_REPORT)}"
    )
    print(
        f"Part 2 Answer: "
        f"{multiply_3_values_that_sum_to_2020(values=EXPENSE_REPORT)}"
    )

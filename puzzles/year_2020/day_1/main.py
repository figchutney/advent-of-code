from typing import Dict, List, Tuple

from .data import EXPENSE_REPORT


def make_values_dict(values: List[int]) -> Dict[int, int]:
    return {value: value for value in values}


def _find_pair_that_sum_to_target(
    values: List[int],
    values_dict: Dict[int, int],
    target: int,
) -> Tuple[int, int]:
    for value in values:
        try:
            return (value, values_dict[target - value])
        except KeyError:
            pass
    raise ValueError(f"Uh oh! No two values sum to {target} :'(")


def _find_triplet_that_sum_to_target(
    values: List[int],
    values_dict: Dict[int, int],
    target: int,
) -> Tuple[int, int, int]:
    for value in values:
        try:
            return (value,) + _find_pair_that_sum_to_target(
                values=values,
                values_dict=values_dict,
                target=target - value,
            )
        except (ValueError, KeyError):
            pass
    raise ValueError(f"Uh oh! No three values sum to {target} :'(")


# PART 1


def multiply_2_values_that_sum_to_2020(
    values: List[int],
    values_dict: Dict[int, int],
) -> int:
    value_1, value_2 = _find_pair_that_sum_to_target(
        values=values,
        values_dict=values_dict,
        target=2020,
    )
    return value_1 * value_2


# PART 2


def multiply_3_values_that_sum_to_2020(
    values: List[int],
    values_dict: Dict[int, int],
) -> int:
    value_1, value_2, value_3 = _find_triplet_that_sum_to_target(
        values=values,
        values_dict=values_dict,
        target=2020,
    )
    return value_1 * value_2 * value_3


if __name__ == "__main__":

    values_dict = make_values_dict(values=EXPENSE_REPORT)

    part_1_answer = multiply_2_values_that_sum_to_2020(
        values=EXPENSE_REPORT,
        values_dict=make_values_dict(values=EXPENSE_REPORT),
    )
    part_2_answer = multiply_3_values_that_sum_to_2020(
        values=EXPENSE_REPORT,
        values_dict=make_values_dict(values=EXPENSE_REPORT),
    )
    print(f"Part 1 Answer: {part_1_answer}")
    print(f"Part 2 Answer: {part_2_answer}")

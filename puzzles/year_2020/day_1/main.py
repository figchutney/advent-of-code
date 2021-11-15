from pathlib import Path
from typing import Set, Tuple


def _make_values_set() -> Set[int]:
    with open(Path(__file__).resolve().parent / "data.txt") as f:
        return {int(value) for value in f}


def _find_pair_that_sum_to_target(
    values: Set[int],
    target: int,
) -> Tuple[int, int]:
    for value in values:
        if (2020 - value) in values:
            return (value, (2020 - value))
    raise ValueError(f"Uh oh! No two values sum to {target} :'(")


def _find_triplet_that_sum_to_target(
    values: Set[int],
    target: int,
) -> Tuple[int, int, int]:
    for value_outer in values:
        for value_inner in values:
            if (2020 - value_outer - value_inner) in values:
                return (
                    value_outer,
                    value_inner,
                    (2020 - value_outer - value_inner),
                )
    raise ValueError(f"Uh oh! No three values sum to {target} :'(")


def solve_part_1(values: Set[int]) -> int:
    value_1, value_2 = _find_pair_that_sum_to_target(
        values=values, target=2020
    )
    return value_1 * value_2


def solve_part_2(values: Set[int]) -> int:
    value_1, value_2, value_3 = _find_triplet_that_sum_to_target(
        values=values, target=2020
    )
    return value_1 * value_2 * value_3


if __name__ == "__main__":

    values = _make_values_set()

    print(f"Part 1 Answer: {solve_part_1(values=values)}")
    print(f"Part 2 Answer: {solve_part_2(values=values)}")

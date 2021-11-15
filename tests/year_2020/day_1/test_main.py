from puzzles.year_2020.day_1 import main

DUMMY_VALUES = {
    1721,
    979,
    366,
    299,
    675,
    1456,
}


def test_solve_part_1() -> None:
    actual = main.solve_part_1(values=DUMMY_VALUES)
    expected = 514579
    assert actual == expected


def test_solve_part_2() -> None:
    actual = main.solve_part_2(values=DUMMY_VALUES)
    expected = 241861950
    assert actual == expected


def test__find_pair_that_sum_to_target() -> None:
    actual = main._find_pair_that_sum_to_target(
        values=DUMMY_VALUES, target=2020
    )
    expected = (1721, 299)
    assert actual == expected


def test__find_triplet_that_sum_to_target() -> None:
    actual = main._find_triplet_that_sum_to_target(
        values=DUMMY_VALUES, target=2020
    )
    expected = (675, 979, 366)
    assert actual == expected

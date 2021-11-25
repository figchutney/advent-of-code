from puzzles.year_2020.day_2 import main

DUMMY_PASSWORD = main.Password(
    policy_letter="m",
    constraint_lower=1,
    constraint_upper=4,
    password="mrfmmbjxr",
)
DUMMY_PASSWORDS = [
    main.Password(
        policy_letter="a",
        constraint_lower=1,
        constraint_upper=3,
        password="abcde",
    ),
    main.Password(
        policy_letter="b",
        constraint_lower=1,
        constraint_upper=3,
        password="cdefg",
    ),
    main.Password(
        policy_letter="c",
        constraint_lower=2,
        constraint_upper=9,
        password="ccccccccc",
    ),
]


def test__parse_password_and_policy() -> None:

    dummy_value = "1-4 m: mrfmmbjxr"

    expected = DUMMY_PASSWORD
    actual = main._parse_password_and_policy(value=dummy_value)

    assert actual == expected


def test__is_letter_count_within_constraints_true() -> None:

    expected = True
    actual = main._is_letter_count_within_constraints(p=DUMMY_PASSWORD)

    assert actual == expected


def test__is_letter_count_within_constraints_false() -> None:

    dummy_password = main.Password(
        policy_letter="x",
        constraint_lower=2,
        constraint_upper=4,
        password="mrfmmbjxr",
    )

    expected = False
    actual = main._is_letter_count_within_constraints(p=dummy_password)

    assert actual == expected


def test__is_letter_in_one_constraint_position_true() -> None:

    dummy_password = main.Password(
        policy_letter="m",
        constraint_lower=1,
        constraint_upper=3,
        password="mrfmmbjxr",
    )

    expected = True
    actual = main._is_letter_in_one_constraint_position(p=dummy_password)

    assert actual == expected


def test__is_letter_in_one_constraint_position_false() -> None:

    expected = False
    actual = main._is_letter_in_one_constraint_position(p=DUMMY_PASSWORD)

    assert actual == expected


def test_solve_part_1() -> None:

    expected = 2
    actual = main.solve_part_1(passwords=DUMMY_PASSWORDS)

    assert actual == expected


def test_solve_part_2() -> None:

    expected = 1
    actual = main.solve_part_2(passwords=DUMMY_PASSWORDS)

    assert actual == expected

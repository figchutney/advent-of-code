from puzzles.year_2020.day_2 import main


def test__parse_password_and_policy() -> None:

    dummy_value = "1-4 m: mrfmmbjxr"

    expected = main.Password(
        required_letter="m",
        letter_count_min=1,
        letter_count_max=4,
        password="mrfmmbjxr",
    )
    actual = main._parse_password_and_policy(value=dummy_value)

    assert actual == expected


def test__is_password_valid_true() -> None:

    dummy_password = main.Password(
        required_letter="m",
        letter_count_min=1,
        letter_count_max=4,
        password="mrfmmbjxr",
    )

    assert main._is_password_valid(password=dummy_password) is True


def test__is_password_valid_false() -> None:

    dummy_password = main.Password(
        required_letter="x",
        letter_count_min=2,
        letter_count_max=4,
        password="mrfmmbjxr",
    )

    assert main._is_password_valid(password=dummy_password) is False


def test_solve_part_1() -> None:

    dummy_passwords = [
        main.Password(
            required_letter="a",
            letter_count_min=1,
            letter_count_max=3,
            password="abcde",
        ),
        main.Password(
            required_letter="b",
            letter_count_min=1,
            letter_count_max=3,
            password="cdefg",
        ),
        main.Password(
            required_letter="c",
            letter_count_min=2,
            letter_count_max=9,
            password="ccccccccc",
        ),
    ]

    expected = 2
    actual = main.solve_part_1(passwords=dummy_passwords)

    assert actual == expected

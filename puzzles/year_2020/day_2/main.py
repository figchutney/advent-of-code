from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class Password:
    required_letter: str
    letter_count_min: int
    letter_count_max: int
    password: str


def _parse_password_and_policy(value: str) -> Password:

    range, letter, password = value.replace(":", "").split(" ")
    min, max = range.split("-")

    return Password(
        required_letter=letter,
        letter_count_min=int(min),
        letter_count_max=int(max),
        password=password,
    )


def _is_password_valid(password: Password) -> bool:

    return (
        password.letter_count_min
        <= password.password.count(password.required_letter)
        <= password.letter_count_max
    )


def make_passwords() -> List[Password]:
    with open(Path(__file__).resolve().parent / "data.txt") as f:
        return [_parse_password_and_policy(value=value) for value in f]


def solve_part_1(passwords: List[Password]) -> int:

    return [
        _is_password_valid(password=password) for password in passwords
    ].count(True)


if __name__ == "__main__":

    passwords = make_passwords()

    print(solve_part_1(passwords=passwords))

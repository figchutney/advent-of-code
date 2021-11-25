from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class Password:
    policy_letter: str
    constraint_lower: int
    constraint_upper: int
    password: str


def _parse_password_and_policy(value: str) -> Password:

    range, letter, password = value.replace(":", "").split(" ")
    lower, upper = range.split("-")

    return Password(
        policy_letter=letter,
        constraint_lower=int(lower),
        constraint_upper=int(upper),
        password=password,
    )


def _is_letter_count_within_constraints(p: Password) -> bool:

    return (
        p.constraint_lower
        <= p.password.count(p.policy_letter)
        <= p.constraint_upper
    )


def _is_letter_in_one_constraint_position(p: Password) -> bool:

    return (
        p.password[p.constraint_lower - 1] == p.policy_letter
        and p.password[p.constraint_upper - 1] != p.policy_letter
    ) or (
        p.password[p.constraint_lower - 1] != p.policy_letter
        and p.password[p.constraint_upper - 1] == p.policy_letter
    )


def make_passwords() -> List[Password]:
    with open(Path(__file__).resolve().parent / "data.txt") as f:
        return [_parse_password_and_policy(value=value) for value in f]


def solve_part_1(passwords: List[Password]) -> int:

    return [
        _is_letter_count_within_constraints(p=password)
        for password in passwords
    ].count(True)


def solve_part_2(passwords: List[Password]) -> int:

    return [
        _is_letter_in_one_constraint_position(p=password)
        for password in passwords
    ].count(True)


if __name__ == "__main__":

    passwords = make_passwords()

    print(solve_part_1(passwords=passwords))
    print(solve_part_2(passwords=passwords))

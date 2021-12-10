from pathlib import Path


def parse_boarding_passes() -> list[str]:
    with open(Path(__file__).resolve().parent / "dummy.txt") as f:
        return [
            pass_.strip("\n")
            .replace("F", "0")
            .replace("B", "1")
            .replace("L", "0")
            .replace("R", "1")
            for pass_ in f
        ]  # e.g. FBFBBFFRLR\n --> 0101100101


def get_seat(pass_: str) -> tuple[int, int]:
    row = int(pass_[:7], 2)
    column = int(pass_[7:], 2)
    return (row, column)


def get_seat_id(pass_: str) -> int:
    row, column = get_seat(pass_=pass_)
    return row * 8 + column


def find_missing_id(ids: list[int]) -> int:
    ids.sort()
    for x, y in zip(ids, ids[1:]):
        if y - x != 1:  # e.g. if y=100, x= 98
            return y - 1  # then missing ID is 99
    raise ValueError("No IDs were missing")


if __name__ == "__main__":

    boarding_passes = parse_boarding_passes()
    print(boarding_passes)
    ids = [get_seat_id(pass_=pass_) for pass_ in boarding_passes]

    # PART 1
    print(max(ids))
    # PART 2
    print(find_missing_id(ids=ids))

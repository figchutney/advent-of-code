from pathlib import Path


def get_depths() -> list[int]:
    with open(Path(__file__).resolve().parent / "data.txt") as f:
        return [int(depth) for depth in f.readlines()]


def count_depth_increases(depths: list[int]) -> int:
    return sum(b > a for a, b in zip(depths, depths[1:]))


def get_window_sums(depths: list[int]) -> list[int]:
    return [a + b + c for a, b, c in zip(depths, depths[1:], depths[2:])]


if __name__ == "__main__":

    depths = get_depths()

    # PART 1
    print(count_depth_increases(depths=depths))
    # PART 2
    print(count_depth_increases(depths=(get_window_sums(depths=depths))))

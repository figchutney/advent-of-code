from pathlib import Path


def make_map() -> list[str]:
    with open(Path(__file__).resolve().parent / "data.txt") as f:
        return [line.strip("\n") for line in f.readlines()]


def is_coordinate_tree(map_: list[str], x: int, y: int) -> bool:
    # Use modulo operator to repeat pattern
    return map_[y][x % len(map_[y])] == "#"


def traverse_map(map_: list[str], right: int, down: int) -> int:

    x, y = (0 + right, 0 + down)  # Don't check (0, 0)
    count = 0

    while y < len(map_):
        count += is_coordinate_tree(map_=map_, x=x, y=y)
        x += right
        y += down

    return count


if __name__ == "__main__":

    map_ = make_map()

    right_3_down_1 = traverse_map(map_=map_, right=3, down=1)
    right_1_down_1 = traverse_map(map_=map_, right=1, down=1)
    right_5_down_1 = traverse_map(map_=map_, right=5, down=1)
    right_7_down_1 = traverse_map(map_=map_, right=7, down=1)
    right_1_down_2 = traverse_map(map_=map_, right=1, down=2)

    # PART 1
    print(right_3_down_1)

    # PART 2
    print(
        right_1_down_1
        * right_3_down_1
        * right_5_down_1
        * right_7_down_1
        * right_1_down_2
    )

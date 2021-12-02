from pathlib import Path

PATH = Path(__file__).resolve().parent / "data.txt"


def calculate_position() -> int:
    with open(PATH) as f:
        (horizontal, vertical) = (0, 0)
        for step in f.readlines():
            direction, distance = step.split(" ")
            if direction == "forward":
                horizontal += int(distance)
            if direction == "down":
                vertical += int(distance)
            if direction == "up":
                vertical -= int(distance)
    return horizontal * vertical


def calculate_position_with_aim() -> int:
    with open(PATH) as f:
        (horizontal, vertical, aim) = (0, 0, 0)
        for step in f.readlines():
            direction, distance = step.split(" ")
            if direction == "forward":
                horizontal += int(distance)
                vertical += aim * int(distance)
            if direction == "down":
                aim += int(distance)
            if direction == "up":
                aim -= int(distance)
    return horizontal * vertical


if __name__ == "__main__":

    # PART 1
    print(calculate_position())
    # PART 2
    print(calculate_position_with_aim())

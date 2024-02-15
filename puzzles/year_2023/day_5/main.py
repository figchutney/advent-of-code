from collections import defaultdict
from pathlib import Path
from typing import Any


def main() -> None:
    with open(Path(__file__).resolve().parent / "example.txt") as f:
        values = [line.strip("\n") for line in f.readlines() if line != "\n"]
    map_: dict[str, list[Any]] = defaultdict(list)
    current_key = None
    for line in values[1:]:
        if "map" in line:
            current_key = line.strip(" map:")
            continue
        map_[current_key].append([int(v) for v in line.split(" ")])
    map_["seeds"] = [int(v) for v in values[0].strip("seeds: ").split(" ")]

    seed_to_soil = {}
    for values in map_["seed-to-soil"]:
        seed_to_soil[]



if __name__ == "__main__":
    main()

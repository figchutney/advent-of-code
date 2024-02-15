from pathlib import Path


def main() -> int:
    with open(Path(__file__).resolve().parent / "example.txt") as f:
        part_1, part_2 = 0, 0
        copies: dict[int, int] = {}
        for c in [line.strip("\n") for line in f.readlines()]:
            w, m = c.split(": ")[1].split(" | ")
            score = len({int(n) for n in w.split()} & {int(n) for n in m.split()})
            part_1 += 2 ** (score - 1) if score > 0 else 0
            copies += score
        return part_1, part_2


if __name__ == "__main__":
    print(main())

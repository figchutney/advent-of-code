import re
from pathlib import Path

WORD_TO_DIGIT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


def main() -> tuple[int, int]:
    with open(Path(__file__).resolve().parent / "input.txt") as f:
        values = [line.strip("\n") for line in f.readlines()]
    return (
        sum(
            int(WORD_TO_DIGIT[n[0]] + WORD_TO_DIGIT[n[-1]])
            for n in [re.findall(r"\d", v) for v in values]
        ),
        sum(
            int(WORD_TO_DIGIT[n[0]] + WORD_TO_DIGIT[n[-1]])
            for n in [
                re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", v)
                for v in values
            ]
        ),
    )


if __name__ == "__main__":
    main()

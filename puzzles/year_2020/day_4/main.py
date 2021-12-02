from pathlib import Path
import re


def parse_passport_details() -> list[dict[str, str]]:
    with open(Path(__file__).resolve().parent / "data.txt") as f:
        return [
            {
                field.split(":")[0]: field.split(":")[1]
                for field in [field for field in passport.split(" ")]
            }
            for passport in (
                passport.replace("\n", " ")
                for passport in f.read().split("\n\n")
            )
        ]


def is_passport_fields_valid(passport: dict[str, str]) -> bool:
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    return required_fields.issubset(set(passport.keys()))


def is_passport_data_valid(passport: dict[str, str]) -> bool:

    byr = passport["byr"]
    iyr = passport["iyr"]
    eyr = passport["eyr"]
    hgt = passport["hgt"]
    hcl = passport["hcl"]
    ecl = passport["ecl"]
    pid = passport["pid"]

    return all(
        (
            len(byr) == 4 and 1920 <= int(byr) <= 2020,
            len(iyr) == 4 and 2010 <= int(iyr) <= 2020,
            len(eyr) == 4 and 2020 <= int(eyr) <= 2030,
            (
                (hgt[-2:] == "cm" and 150 <= int(hgt[:-2]) <= 193)
                or (hgt[-2:] == "in" and 59 <= int(hgt[:-2]) <= 76)
            ),
            re.fullmatch(r"#[(0-9)|(a-f)]{6}", hcl),
            ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
            re.fullmatch(r"\d{9}", pid),
        )
    )


if __name__ == "__main__":

    passports = parse_passport_details()

    passports_valid_fields = [
        passport
        for passport in passports
        if is_passport_fields_valid(passport=passport)
    ]
    passports_valid_data = [
        passport
        for passport in passports_valid_fields
        if is_passport_data_valid(passport=passport)
    ]

    # PART 1
    print(len(passports_valid_fields))
    # PART 2
    print(len(passports_valid_data))

from pathlib import Path

if __name__ == "__main__":

    with open(Path(__file__).resolve().parent / "data.txt") as f:
        passwords = [line for line in f]

    valid_passwords_part_1 = 0
    valid_passwords_part_2 = 0

    for string in passwords:

        range, letter, password = string.replace(":", "").split(" ")
        value_1, value_2 = range.split("-")

        # PART 1
        if int(value_1) <= password.count(letter) <= int(value_2):
            valid_passwords_part_1 += 1

        # PART 2
        if (
            password[int(value_1) - 1] == letter
            and password[int(value_2) - 1] != letter
        ) or (
            password[int(value_1) - 1] != letter
            and password[int(value_2) - 1] == letter
        ):
            valid_passwords_part_2 += 1

    # PART 1
    print(valid_passwords_part_1)
    # PART 2
    print(valid_passwords_part_2)

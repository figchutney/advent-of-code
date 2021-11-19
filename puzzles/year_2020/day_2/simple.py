from pathlib import Path

if __name__ == "__main__":

    with open(Path(__file__).resolve().parent / "data.txt") as f:
        passwords = [line for line in f]

    # PART 1
    valid_passwords = 0
    for string in passwords:
        range, letter, password = string.replace(":", "").split(" ")
        min, max = range.split("-")
        if int(min) <= password.count(letter) <= int(max):
            valid_passwords += 1

    print(valid_passwords)

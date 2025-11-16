def write_lines(filename: str, lines: list):
    # Write each string on a new line
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")


def read_lines(filename: str) -> list:
    # Read file and remove newline characters
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    write_lines("sample.txt", ["hello", "world"])
    print(read_lines("sample.txt"))


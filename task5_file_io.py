"""
TASK 5: FILE I/O

Write two functions:

1. write_lines(filename, lines)
   - Takes a filename and a list of strings
   - Writes each string to a new line in the file

2. read_lines(filename)
   - Reads file and returns a list of lines without newline characters

Example:
write_lines("test.txt", ["hello", "world"])
read_lines("test.txt") → ["hello", "world"]
"""

def write_lines(filename: str, lines: list):
    # Your code here
    pass


def read_lines(filename: str) -> list:
    # Your code here
    pass


if __name__ == "__main__":
    write_lines("sample.txt", ["hello", "world"])
    print(read_lines("sample.txt"))

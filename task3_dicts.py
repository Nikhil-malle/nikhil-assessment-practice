"""
TASK 3: DICTIONARY TRANSFORMATION

You are given a dictionary of student scores:

students = {"nikhil": 88, "akhil": 92, "varun": 75}

Write a function `passed_students(data, threshold)` that:
- Returns a new dictionary containing only students who scored >= threshold

Example:
passed_students(students, 80) → {"nikhil": 88, "akhil": 92}
"""

def passed_students(data: dict, threshold: int) -> dict:
    # Your code here
    pass


if __name__ == "__main__":
    students = {"nikhil": 88, "akhil": 92, "varun": 75}
    print(passed_students(students, 80))

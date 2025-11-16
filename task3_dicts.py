def passed_students(data: dict, threshold: int) -> dict:
    # Return only students with score >= threshold
    return {name: score for name, score in data.items() if score >= threshold}


if __name__ == "__main__":
    students = {"nikhil": 88, "akhil": 92, "varun": 75}
    print(passed_students(students, 80))


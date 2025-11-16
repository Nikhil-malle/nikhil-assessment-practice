def unique_sorted(numbers: list) -> list:
    # Remove duplicates using a set, then sort
    return sorted(set(numbers))


if __name__ == "__main__":
    print(unique_sorted([5, 3, 5, 2, 1]))

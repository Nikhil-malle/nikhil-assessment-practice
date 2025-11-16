def first_unique_char(s: str):
    # Count occurrences of each character
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Find the first character with frequency 1
    for ch in s:
        if freq[ch] == 1:
            return ch

    return None


if __name__ == "__main__":
    print(first_unique_char("aabbcde"))  # Output: c
    print(first_unique_char("aabb"))     # Output: None

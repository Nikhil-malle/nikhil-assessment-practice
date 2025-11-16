def clean_sentence(text: str) -> str:
    # Remove leading/trailing spaces
    text = text.strip()
    # Replace multiple spaces with a single space
    text = " ".join(text.split())
    # Capitalize first letter
    text = text.capitalize()
    return text


if __name__ == "__main__":
    print(clean_sentence("   hello    world  "))


def main() -> None:
    s = input("Enter a line: ")
    while s:
        print(f"Is that string a palindrome? {'Yes!' if is_palindrome(s) else 'No.'}")
        s = input(": ")


def is_palindrome(s: str, start: int = -1, end: int = -1) -> bool:
    if len(s) < 1:
        return True
    elif start < 0 or end < 0:
        return is_palindrome(s, 0, len(s) - 1)

    if s[start] != s[end]:
        return False
    elif start >= end:  # middle
        return True

    return is_palindrome(s, start + 1, end - 1)


if __name__ == "__main__":
    main()

def is_palindrome(string: str) -> bool:
    is_valid_character = lambda char: (
        'a' <= char <= 'z' or
        'A' <= char <= 'Z' or
        '0' <= char <= '9'
    )

    l, r = 0, len(string) - 1

    while l < r:
        while not is_valid_character(string[l]):
            l += 1
        while not is_valid_character(string[r]):
            r -= 1

        if string[l].lower() != string[r].lower():
            return False

        l += 1
        r -= 1

    return True

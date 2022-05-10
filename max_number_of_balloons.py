def max_number_of_balloons(text: str) -> int:
    char_idx = lambda c: ord(c) - ord('a')
    alphabet_count = [0] * 26

    for char in text:
        alphabet_count[char_idx(char)] += 1

    max_balloons_generated = alphabet_count[char_idx('b')]
    max_balloons_generated = min(
        max_balloons_generated,
        alphabet_count[char_idx('a')]
    )
    max_balloons_generated = min(
        max_balloons_generated,
        alphabet_count[char_idx('l')] // 2
    )
    max_balloons_generated = min(
        max_balloons_generated,
        alphabet_count[char_idx('o')] // 2
    )
    max_balloons_generated = min(
        max_balloons_generated,
        alphabet_count[char_idx('n')]
    )

    return max_balloons_generated

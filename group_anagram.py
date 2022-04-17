def group_anagram(strs: list):
    """Returns a list of grouped anagrams

    Args:
        strs (List[str]): List of input strings
    
    Returns:
        list of listed strings
    """

    def letter_count_arr(s: str) -> list:
        """Returns a letter count of how many times a-z appears
        in a string defined by @s

        Args:
            s (str): string

        Returns:
            list with counts occurrences of 'a' - 'z'
        """
        letter_count = [0] * 26
        for letter in string:
            letter_count[
                ord(letter) - ord('a')
            ] += 1
        return letter_count

    anagrams = {}

    for string in strs:
        key = tuple(
            letter_count_arr(string)
        )
        anagrams[key] = anagrams.get(key, []) + [string]

    return [
        anagram
        for anagram in anagrams.values()
    ]

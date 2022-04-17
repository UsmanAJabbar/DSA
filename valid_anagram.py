# Idea:
# To ensure we have a valid anagram,
# we need to make sure we have the exact amount of characters

# So, we could simply count the occurrences of letters in s
# and compare if they occurred the same amount of time in t

# But let's say we have the same amount of characters in s and t
# but we have extra keys in s or t, we could compare the amount
# of letters just in case

def valid_anagram(s: str, t: str) -> bool:
    """
    -------------
    Valid Anagram
    -------------
    Given two strings s and t,
    return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the
    letters of a different word or phrase, typically using all
    the original letters exactly once.
    """
    def count_letters_in_string(string: str) -> dict:
        letter_count = {}

        for letter in string:
            letter_count[letter] = letter_count.get(letter, 0) + 1

        return letter_count

    s_count = count_letters_in_string(s)
    t_count = count_letters_in_string(t)

    return (
        len(s_count) == len(t_count)
        and s_count == t_count
    )

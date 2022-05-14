def longest_substring_wo_repeating_characters_1(s: str) -> int:
    l = 0
    r = 0
    charset = set()
    order = []
    max_len = 0
    while l <= r and r <= len(s) - 1:
        if s[r] not in charset:
            order.append(s[r])
            charset.add(s[r])
            r += 1
        else:
            while s[l] != s[r]:
                charset.remove(order.pop(0))
                l += 1
            charset.remove(order.pop(0))
            l += 1
        max_len = max(len(charset), max_len)

    return max_len

def longest_substring_wo_repeating_characters_2(s: str) -> int:
    l = 0
    charset = set()
    max_len = 0

    for r in range(len(s)):
        while s[r] in charset:
            charset.remove(s[l])
            l += 1
        charset.add(s[r])
        max_len = max(
            max_len, r - l + 1
        )

    return max_len

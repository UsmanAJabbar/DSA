class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        ----------------------------------------------
        LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
        ----------------------------------------------
        Description:
            Given a string `s`, find the length of the longest substring without repeating characters.

            Source: https://leetcode.com/problems/longest-substring-without-repeating-characters
        """
        subset_chars = set()
        max_substring_len = 0

        l, r = 0, 0
        while r < len(s):
            if s[r] not in subset_chars:
                subset_chars.add(s[r])
                r += 1
                max_substring_len = max(max_substring_len, r - l)
            else:
                while s[r] in subset_chars:
                    subset_chars.remove(s[l])
                    l += 1

        return max_substring_len
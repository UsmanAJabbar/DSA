#!/usr/bin/env python3


def longest_consecutive_sequence(nums) -> int:
    nums = set(nums)
    longest_sequence = 0
    
    for n in nums:
        # Check if we're possibly at the beginning of a streak
        if n - 1 not in nums:
            longest_subsequence = 1
            while n + longest_subsequence in nums:
                longest_subsequence += 1
            longest_sequence = max(longest_sequence, longest_subsequence)

    return longest_sequence

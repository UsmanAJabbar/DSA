from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        -------------------------
        CONTAINER WITH MOST WATER
        -------------------------
        Description:
            You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

            Find two lines that together with the x-axis form a container, such that the container contains the most water.

            Return the maximum amount of water a container can store.

            Source: https://leetcode.com/problems/container-with-most-water/
        """
        l, r = 0, len(height) - 1
        
        global_max = 0

        while l < r:
            pillar_l, pillar_r = height[l], height[r]

            local_max = min(pillar_l, pillar_r) * (r - l)
            global_max = max(local_max, global_max)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return global_max
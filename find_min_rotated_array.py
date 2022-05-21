def min_rotated_array(nums: list, target: int):
    # If the array isn't rotated, the first value must be the smallest
    if nums[0] < nums[-1]: return nums[0]

    l, r = 0, len(nums) - 1

    min_value = float('inf')

    while l <= r:
        mid_idx = (l + r) // 2

        min_value = min(min_value, nums[mid_idx])

        # Search for the pivot since we know pivot == min_value
        if nums[mid_idx] > nums[r]:
            l = mid_idx + 1
        else:
            r = mid_idx - 1

    return min_value

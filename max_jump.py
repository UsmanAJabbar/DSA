def canJump(nums: list) -> bool:
    l = 0
    r = 0

    # This is the index we need to reach
    goal_post = len(nums) - 1

    # R will act as the maximum index that's possible to reach
    # L will increment by 1 as usual
    # With every increment of L, we will check
    # and update whether we could reach a farther r
    while l <= r and l < goal_post:
        r = max(nums[l] + l, r)
        l += 1

    return r >= goal_post

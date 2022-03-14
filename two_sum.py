def two_sum_hashed(nums, target):
    # PLAN
    # target is supposed to made up of two numbers
    # Equation: x + y = target

    # We need to find the x and the y that make up target
    # and return their indexes

    # We'll rearrange the above equation to
    # target = n + y or
    # target - n = y or
    # y = target - n

    # With every loop, we'll try to get y and see if
    # we ever came across an n before.
    # If we haven't we'll add the current n to the cache such that
    # later on, we could check if we ever came across an n that when added
    # makes up target, we're bingo

    # n + y = target
    # Return indexes

    cache = {}
    for idx, n in enumerate(nums):
        y = target - n
        if y in cache:
            return [ idx, cache[y] ]
        else:
            cache[n] = idx

    return []

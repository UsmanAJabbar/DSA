def climb_stairs_recursive(n: int) -> int:
    cache = {}
    def helper(n: int) -> int:
        # Returns 1 if the path to 0 was valid
        # Else returns 0 if the past wasn't valid
        if n == 0: return 1
        if n  < 0: return 0

        if n - 1 not in cache:
            cache[n - 1] = helper(n - 1)
        if n - 2 not in cache:
            cache[n - 2] = helper(n - 2)

        return (
            cache[n - 2] + cache[n - 1]
        )
    return helper(n)


def climb_stairs_iterative(n: int) -> int:
    """
    For this to work, instead of creating an array,
    we instead decided to use two variables that keep
    track of the past two numbers
    """
    f_n_2 = 0
    f_n_1 = 1

    for _ in range(n):
        f_n = f_n_2 + f_n_1
        f_n_2 = f_n_1
        f_n_1 = f_n

    return f_n


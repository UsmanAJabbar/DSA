def coin_change_2(coins: list, amount: int) -> int:
    lookup = {}

    def backtrack(idx: int, amount: int) -> int:
        if amount < 0 or idx >= len(coins):
            return 0
        if amount == 0:
            return 1

        # count(idx, total) = (
        #   count(idx, total - coin[idx]) +
        #   count(idx + 1, total)
        # )

        key = (idx, amount)
        if key not in lookup:
            incl = backtrack(idx, amount - coins[idx])
            excl = backtrack(idx + 1, amount)
            lookup[key] = incl + excl

        return lookup[key]

    return backtrack(0, amount)

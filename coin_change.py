def coin_change(coins: list, amount: int) -> int:
    basecase = float('inf')
    dp = [basecase] * (amount + 1)
    dp[0] = 0

    for value in range(amount + 1):
        for coin_choice in coins:
            if coin_choice <= value:
                dp[value] = min(
                    dp[value],
                    dp[value - coin_choice] + 1
                )

    if dp[value] == basecase:
        return -1

    return dp[value]

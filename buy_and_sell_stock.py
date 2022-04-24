def sell_stock(prices):
    max_profit_achieved = 0
    min_price = prices[0]

    for price in prices:
        current_profit = price - min_price

        max_profit_achieved = max(
            max_profit_achieved,
            current_profit
        )
        min_price = max(
            min_price,
            price
        )

    return max_profit_achieved

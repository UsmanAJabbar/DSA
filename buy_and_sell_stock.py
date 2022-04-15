def sell_stock(prices):
    max_profit_achieved = 0
    min_price = prices[0]

    for price in prices:
        current_profit = price - min_price

        if current_profit > max_profit_achieved:
            max_profit_achieved = current_profit
        if price < min_price:
            min_price = price

    return max_profit_achieved

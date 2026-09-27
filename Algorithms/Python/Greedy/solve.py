def greedy(coins, target):
    sorted_coins = sorted(coins, reverse=True)

    change = []
    left_money = target

    for coin in sorted_coins:
        while left_money >= coin:
            change.append(coin)
            left_money -= coin

        if left_money == 0:
            break

    if left_money > 0:
        return "No es posible dar el cambio exacto con estas monedas"

    return change 
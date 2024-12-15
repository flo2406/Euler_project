def coin_sum_rec(value, coins):
    res = 0
    for i, coin in enumerate(coins):
        if value == coin:
            res += 1
        elif value > coin:
            res += coin_sum_rec(value - coin, coins[i:])
    return res

def coin_sum():
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    return coin_sum_rec(200, coins)

print(coin_sum())
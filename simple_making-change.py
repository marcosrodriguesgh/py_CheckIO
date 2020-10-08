def checkio(price, denominations):
    """
        return the minimum number of coins that add up to the price
    """
    tmp_price = price
    coins = 0
    tup = []
    for i in reversed(denominations):
        coins += tmp_price // i
        tmp_price -= (tmp_price // i) * i
        if price % i == 0:
            tup.append(price//i)
        print('coin : ', i)
        print('coins: ', coins)
        print('price: ', tmp_price)
        print('tup',tup)
    coins = min(coins, min(tup) if tup else coins)
    return None if tmp_price else coins


if __name__ == '__main__':
    print("Example:")
    print(checkio(1,[3,4,5]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(8, [1, 3, 5]) == 2
    print('=========================')
    assert checkio(12, [1, 4, 5]) == 3
    print('Done')

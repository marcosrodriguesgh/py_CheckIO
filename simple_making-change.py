def checkio(price, denominations):
    """
        return the minimum number of coins that add up to the price
    """
    coinsTup = denominations
    coinsFinal = price
    for j in range(len(coinsTup)):
        tmp_price = price
        coins = 0
        for i in reversed(coinsTup):
            coins += tmp_price // i
            tmp_price -= (tmp_price // i) * i
            print('coin : ', i)
            print('coins: ', coins)
            print('price: ', tmp_price)
        if tmp_price == 0 and coins < coinsFinal:
            coinsFinal = coins
        coinsTup.pop()
    return None if coinsFinal == price else coinsFinal


if __name__ == '__main__':
    # print("Example:")
    # print(checkio(1,[3,4,5]))
    #
    # # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio(8, [1, 3, 5]) == 2
    # print('=========================')
    # assert checkio(12, [1, 4, 5]) == 3
    assert checkio(123456,[1,6,7,456,678]) == 187
    print('Done')

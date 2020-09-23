def checkio(number):
    pingeons = 1
    food_line = []
    while number:
        for i in range(pingeons):
            food_line.append(0)
        for i, j in enumerate(food_line):
            if number:
                food_line[i] = j + 1
                number -= 1
            else:
                break
        pingeons += 1
    return len(food_line) - food_line.count(0)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
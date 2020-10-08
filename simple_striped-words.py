def checkio(line: str) -> str:
    Vowels = 'AEIOUY'
    Consonants = 'BCDFGHJKLMNPQRSTVWXZ'
    testV = line[0] in Vowels
    testC = line[0] in Consonants
    testO = num = 0
    for i, l in enumerate(line.upper()):
        if l in Vowels and i > 0:
            testV += 1
            testC -= 1
            testO = 0
            if testV == 2 or testC == 2:
                testV = testC = 0
                pass
        elif l in Consonants:
            testV -= 1
            testC += 1
            testO = 0
            if testV == 2 or testC == 2:
                testV = testC = 0
                pass
        else:
            testO += 1
            if -1 < testC <= 1 and -1 < testV <= 1 and testO == 1:
                num += 1
                testV = testC = 0

        print('letra = ', l, 'testV = ', testV, 'testC = ', testC)
    print(num)
    return num


if __name__ == '__main__':
    print("Example:")
    print(checkio('My name is ...'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('My name is ...') == 3
    assert checkio('Hello world') == 0
    assert checkio('A quantity of striped words.') == 1
    assert checkio('Dog,cat,mouse,bird.Human.') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")

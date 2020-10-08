def checkio(data):
    romans = {'M': 1000,'D': 500,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    output = ''
    prev = ('M','')
    for x, y in romans.items():
        prev = (x, prev[0])
        print(data)
        if str(data)[0] == '4' and int(data//y) > 0:# and x not in 'VLD':
            output += x + prev[0]
        elif str(data)[0] == '9' and int(data // y) > 0:
            if x in 'VLD':
                continue
            output += x + prev[1]
        else:
            output += x * int(data//y)
        print(output)

        print(prev)
        data -= (data // y) * y
    print('-----------------------------')
    return output

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
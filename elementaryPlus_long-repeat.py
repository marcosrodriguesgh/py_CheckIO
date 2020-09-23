def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    if line:
        cont = maxi = 1
        elem = line[0]
        for i in line[1:]:
            if elem == i:
                cont += 1
                maxi = cont if cont > maxi else maxi
            else:
                maxi = cont if cont > maxi else maxi
                elem = i
                cont = 1
        return maxi
    else:
        return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')

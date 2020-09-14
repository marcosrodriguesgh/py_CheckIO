def nearest_value(values: set, one: int) -> int:
    lista = list(values)
    if len(lista) == 1:
        return lista[0]
    lista.append(one)
    lista = sorted(lista)
    if one == lista[0]: # covering the list borders
        return lista[1]
    elif one == lista[-1]: # covering the list borders
        return lista[-2]
    else:
        index = lista.index(one)
        return lista[index-1] if abs(lista[index-1] - one) <= abs(lista[index+1] - one) else lista[index+1]


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")

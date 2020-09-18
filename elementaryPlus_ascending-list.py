from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    '''
    Determine whether the sequence of elements items is ascending so that its each element
    is strictly larger than (and not merely equal to) the element that precedes it.
    :param items: Iterable with ints
    :return: Bool
    '''
    # Minhas solução---------------------------------
    # for i in items:
    #     if items.count(i) > 1:
    #         return False
    # return sorted(items) == items

    # Solução Otimizada -----------------------------
    return all(items[i] < items[i+1] for i in range(len(items)-1))

if __name__ == '__main__':
    print("Example:")
    print(is_ascending([-5, 10, 99, 123456]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

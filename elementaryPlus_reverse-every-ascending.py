def reverse_ascending(items):
    output = []
    ind = [0]
    for x in range(1, len(items)):
        if items[x-1] >= items[x]:
            ind.append(x)
    if len(ind) == 1:
        return sorted(items, reverse=True)
    else:
        for i in range(len(ind)-1):
            output = output + sorted(items[ind[i]:ind[i+1]], reverse=True)
    return output + sorted(items[ind[-1]:], reverse=True)


if __name__ == '__main__':
    print("Example:")
    print(reverse_ascending([1, 2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

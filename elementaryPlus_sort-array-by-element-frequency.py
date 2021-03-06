def frequency_sort(items):
    dic = {}
    tup = []
    for i in items:
        if i not in dic:
            dic.update({i: 1})
        else:
            dic.update({i: dic[i] + 1})
    for x in sorted(dic.items(), key=lambda t: t[1], reverse=True):
        for _ in range(x[1]):
            tup.append(x[0])
    return tup


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4]))
    #print(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    # assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    # assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    # assert list(frequency_sort([])) == []
    # assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

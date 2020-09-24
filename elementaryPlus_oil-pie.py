def divide_pie(groups):
    from fractions import Fraction
    group = sum([abs(x) for x in groups])
    remain_pie = Fraction(1, 1)
    for i in groups:
        if i > 0:
            remain_pie -= Fraction(i, group)
        else:
            remain_pie -= remain_pie * Fraction(abs(i), group)
    return remain_pie.as_integer_ratio()


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"

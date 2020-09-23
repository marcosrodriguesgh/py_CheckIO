def checkio(radius):
    """count tiles"""
    from math import hypot, ceil
    if radius % 1 > 0:
        hipotenuse = hypot(radius, radius)
        if hipotenuse <
        if (radius // 1) + hipotenuse > radius:
            solid = ((radius // 1 - 1) * 2) ** 2
            print(1111111111)
            return [solid, (ceil(radius) * 2) ** 2 - solid]
        else:
            return [solid, 0]
    else:
        solid = ((radius - 1) * 2) ** 2
        return [solid, (radius * 2) ** 2 - solid]
    return [0, 0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"

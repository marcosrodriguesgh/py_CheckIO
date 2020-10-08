def safe_pawns(pawns: set) -> int:
    colluns = 'xabcdefghx'
    safe = 0
    for p in pawns:
        if p[1] != '1':
            collunIndex = colluns.index(p[0])
            prev = colluns[collunIndex-1]
            next = colluns[collunIndex+1]
            safe += list(pawns).count(prev + str(int(p[1])-1))
            if not list(pawns).count(prev + str(int(p[1])-1)):
                safe += list(pawns).count(next + str(int(p[1])-1))
    return safe

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

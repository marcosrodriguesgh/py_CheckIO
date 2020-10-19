def middle(text):
    mid = len(text) // 2
    return text[mid:mid+1] if len(text) % 2 else text[mid-1:mid+1]

if __name__ == '__main__':
    print("Example:")
    print(middle('example'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert middle('example') == 'm'
    assert middle('test') == 'es'
    assert middle('very-very long sentence') == 'o'
    assert middle('I') == 'I'
    assert middle('no') == 'no'
    print("Coding complete? Click 'Check' to earn cool rewards!")

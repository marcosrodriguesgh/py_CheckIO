def time_converter(time):
    return str(int(time[0:2]) if int(time[0:2]) < 13 and time[0:2] != '00' else abs(int(time[0:2]) - 12)) \
           + time[2:] \
           + (' a.m.' if int(time[0:2]) < 12 else ' p.m.')


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")

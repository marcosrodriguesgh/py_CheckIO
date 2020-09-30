def sun_angle(time):
    timeInMinutes = int(time.split(':')[0])*60 + int(time.split(':')[1])
    return "I don't see the sun!" if timeInMinutes < 60*6 or timeInMinutes > 60*18 else (timeInMinutes-60*6) * 0.25

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")

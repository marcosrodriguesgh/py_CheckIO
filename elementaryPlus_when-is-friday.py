import datetime

def friday(day):
    fridayNum = 4
    dayList = day.split('.')
    weekDay = datetime.datetime(int(dayList[2]),int(dayList[1]),int(dayList[0])).weekday()
    return fridayNum - weekDay if weekDay <= fridayNum else 7 % weekDay + 4

if __name__ == '__main__':
    # print("Example:")
    # print(friday('23.04.2018'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert friday('23.04.2018') == 4
    assert friday('01.01.1999') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")

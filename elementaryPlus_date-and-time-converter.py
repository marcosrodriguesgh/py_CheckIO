def date_time(time: str) -> str:
    monthDic = {'01': 'January', '02': 'February','03': 'March','04': 'April','05': 'May','06': 'June',
'07': 'July','08': 'August','09': 'September','10': 'October','11': 'November','12': 'December'}
    # print(f'{int(time[0:2])} {monthDic[time[3:5]]} {time[6:10]} year {int(time[11:13])} {"hour" if int(time[11:13]) == 1 else "hours"} {int(time[-2:])} {"minute" if int(time[-2:])==1 else "minutes"}')
    return f'{int(time[0:2])} {monthDic[time[3:5]]} {time[6:10]} year {int(time[11:13])} {"hour" if int(time[11:13]) == 1 else "hours"} {int(time[-2:])} {"minute" if int(time[-2:])==1 else "minutes"}'

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")

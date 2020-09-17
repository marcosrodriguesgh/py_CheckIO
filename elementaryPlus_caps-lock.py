def caps_lock(text: str) -> str:
    # output = text.split('a')
    # for i in range(len(output)):
    #     if i % 2 == 1:
    #         output[i] = output[i].upper()
    # return ''.join(output)
    return ''.join(c.upper() if i % 2 == 1 else c for i, c in enumerate(text.split('a')))


if __name__ == '__main__':
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    print("Coding complete? Click 'Check' to earn cool rewards!")

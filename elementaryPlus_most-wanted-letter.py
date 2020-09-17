def checkio(text: str) -> str:
    from string import ascii_lowercase
    dic = {i: text.lower().count(i) for i in text.lower() if i in ascii_lowercase}
    maxk = sorted(k for k, v in dic.items() if v == max(dic.values()))
    return maxk[0]

if __name__ == '__main__':
    print("Example:")
    print(checkio("AAaooo!!!!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

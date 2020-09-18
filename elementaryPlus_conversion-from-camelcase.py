def from_camel_case(name):
    '''
    Your mission is to convert the name of a function (a string) from CamelCase ("MyFunctionName") into the Python
    format ("my_function_name") where all chars are in lowercase and all words are concatenated with an intervening
    underscore symbol "_". Input data won't contain any numbers.
    :param name: A function name as a CamelCase string.
    :return: The same string, but in under_score.
    Precondition:
    0 < len(string) <= 100
    '''
    for i, l in enumerate(name):
        if l.isupper() and i > 0:
            name = name.replace(l,  '_' + l)
    return name.lower()


if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("MyFunctionName"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
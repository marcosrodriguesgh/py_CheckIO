def checkio(in_string):
    import unidecode
    # accents_list = ('à', 'é', 'ô', 'ñ', 'è', 'ă', 'ớ', 'ö', 'àeìǹòùẁỳÀÈÌǸÒÙẀỲ')
    # naccents_list = ('a', 'e', 'o', 'n', 'e', 'a', 'o', 'o')
    # # print('á'.encode(encoding='ascii'))
    # for i in range(len(accents_list)):
    #     in_string = in_string.replace(accents_list[i], naccents_list[i])
    # print(in_string)
    print('à'.is=='a'.isascii())
    return in_string

    # These "asserts" using only for self-checking and not necessary for auto-testing


if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')

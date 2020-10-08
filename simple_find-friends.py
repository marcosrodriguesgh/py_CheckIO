def check_connection(network, first, second):
    tup = ['']
    nottup = []
    func = lambda net, f: [x for x in net if f in x]
    f = first
    i = 0
    tam = 1000
    while tup and i <= tam:
        tup = func(network, f)
        print(tup)
        if len(tup):
            tup = [x.replace(f, '').replace('-', '') for x in tup]
            # tam = tup.count(f)
            print('-->', tup)
            if tup.count(second):
                return True
            f = tup[0]
            i += 1
    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "scout2", "scout3") == True, "Scout Brotherhood"
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "super", "scout2") == True, "Super Scout"
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "dr101", "sscout") == False, "I don't know any scouts."
    assert check_connection(("scout2-plane1","plane1-stevan","stevan-night","night-mega","mega-sscout","sscout-super","super-scout3","scout3-doc","doc-batman",),"scout2","batman") == True

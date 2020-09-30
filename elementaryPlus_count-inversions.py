def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    lista = list(sequence)
    count = 0
    while True:
        if lista != sorted(lista):
            for i in range(1, len(lista)):
                if lista[i-1] > lista[i]:
                    lista[i - 1], lista[i] = lista[i], lista[i-1]
                    count += 1
        else:
            break
    return count

if __name__ == '__main__':
    print("Example:");
    print(count_inversion([1, 2, 5, 3, 4, 7, 6]));

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

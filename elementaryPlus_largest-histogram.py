def largest_histogram(histogram):
    if len(histogram) == 1:
        return histogram[0]
    # elif len(histogram) == 2:
    #     return min(histogram) * 2
    maxi = histogram[0]
    print(histogram)
    for i in range(0, len(histogram)-1):
        newmaxi = max([min(histogram[i:i+2]) * 2, histogram[i], histogram[-1], len(histogram)])
        print('i = ', i)
        print('1 - ', min(histogram[i:i+2]) * 2, ' - ', histogram[i:i+1], ' - ', min(histogram[i:i+1]))
        print('2 - ', histogram[i])
        print('3 - ', histogram[-1])
        print('4 - ', len(histogram))
        print(newmaxi)
        maxi = newmaxi if newmaxi > maxi else maxi
    print(histogram)
    return maxi


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")

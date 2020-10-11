def checkio(text, word):
    text_list = text.replace(' ', '').lower().split('\n')

    # horizontal search
    for i, x in enumerate(text_list, start=1):
        if x.count(word):
            return [i, x.index(word)+1, i, x.index(word)+len(word)]

    # vertical search
    num_find = []
    for i, x in enumerate(text_list):       # loop every line
        for j, char in enumerate(x):        # loop every char in line to find occurrences of first char of the word
            if char == word[0]:
                num_find.append(j)          # save the index of occurrences in a list
        if num_find:                        # if occurrences exist
            for c in num_find:              # loop for every occurrences
                word_index = 1
                for line in text_list[i+1:]:  # loop every line after the line of found occurrence
                    if line[c] != word[word_index]:
                        break
                    word_index += 1
                    if word_index >= len(word)-1:
                        return [i+1, c+1, i+len(word), c+1]
        num_find = []

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
    assert checkio('xa\nxb\nx', 'ab')
print("Coding complete? Click 'Check' to earn cool rewards!")

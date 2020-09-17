def is_stressful(subj):
    """
        recognize stressful subject
    """
    from string import punctuation
    newSubj = ''
    for i in range(len(subj)-1):
        if subj[i].lower() != subj[i+1].lower() and subj[i] not in punctuation:
            newSubj += subj[i].lower()
    if subj[-1] not in punctuation:
        newSubj += subj[-1].lower()
    if len(set(newSubj.split()).intersection(['help', 'asap', 'urgent'])) > 0 or subj.isupper() or subj.endswith('!!!'):
        return True
    else:
        return False


if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    is_stressful('We need you A.S.A.P.!!')
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')

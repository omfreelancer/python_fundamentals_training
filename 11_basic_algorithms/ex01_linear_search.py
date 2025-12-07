def linear_search(lst, target):
    i = 0
    for item in lst:
        if item == target:
            return i
        i += 1

    return -1
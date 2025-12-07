def find_min(lst):
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num

    return smallest

def find_max(lst):
    biggest = lst[0]
    for num in lst:
        if num > biggest:
            biggest = num

    return biggest

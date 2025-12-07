def binary_search(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        middle_value = lst[mid]

        if middle_value == target:
            return mid

        elif middle_value > target:
            high = mid -1

        else:
            low = mid +1
    
    return -1
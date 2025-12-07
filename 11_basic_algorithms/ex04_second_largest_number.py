def second_largest(lst):
    if len(lst) < 2:
        return None
    
    largest = float("-inf")
    second = float("-inf")
    for number in lst:
        if number > largest:
            second = largest
            largest = number

        else:
            if number != largest and number > second:
                second = largest

    if second == float("-inf"):
        return None

    return second
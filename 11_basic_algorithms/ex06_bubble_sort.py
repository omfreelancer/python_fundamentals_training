def bubble_sort(lst):
    if len(lst) < 2:
        return lst
    
    while True:
        swapped = False
        for i in range(0, len(lst) -1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True

        if not swapped:
            return lst
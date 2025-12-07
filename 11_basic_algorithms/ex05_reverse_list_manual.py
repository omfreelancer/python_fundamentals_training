def reserve_list_range(lst):
    if len(lst) < 2:
        return lst
    
    new_list = []
    for i in range(len(lst)-1,-1,-1):
        new_list.append(lst[i])

    return new_list

def reserve_list_insert(lst):
    if len(lst) < 2:
        return lst
    
    new_list = []
    for item in lst:
        new_list.insert(0, item)

    return new_list
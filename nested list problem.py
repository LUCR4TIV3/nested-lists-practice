lst1 = [[2, 'a', 3], ['b', 5, 6], ['x', 'y'], [7]]
def transform_nested_list(lst):
    result = []
    for innerlist in lst:
        newlist = []
        for i in innerlist:
            if isinstance(i, int):
                newlist.append(i**2)
        if newlist:
            result.append(newlist)
    return result
print(transform_nested_list(lst1))



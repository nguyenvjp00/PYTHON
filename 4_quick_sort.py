def sort(list):
    length = len(list)
    if length <= 1:
        return list
    else:
        pivot = list.pop()
    items_greater = []
    items_lower = []

    for item in list:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return sort(items_lower) + [pivot] + sort(items_greater)

list = [2, 8, 3, 7, 9, 5, 1, 4]
sort(list)
print(sort(list))

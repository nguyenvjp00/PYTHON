def sort(list):
    length = range(1, len(list))
    for i in length:
        value_to_sort = list[i]
        while list[i - 1] > value_to_sort and i > 0:
            list[i], list[i - 1] = list[i - 1], list[i]
            i = i - 1
    return list


list = [5, 2, 3, 7, 4, 1]
sort(list)
print(list)

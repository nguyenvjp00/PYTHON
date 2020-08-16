def sort(list):
    for i in range(len(list)):
        minpos = i
        for j in range(i, len(list)):
            if list[j] < list[minpos]:
                minpos = j

        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = list[i]


list = [24, 67, 16, 885, 23, 875, 232, 1]
sort(list)

print(list)

def sapxep(list):
    in_length = len(list)
    if in_length < 1:
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
    return sapxep(items_lower) + [pivot] + sapxep(items_greater)


list = []
print("Nhập vào số phần tử của mảng: ")
n = int(input())
print("Nhập vào các phần tử của mảng: ")
for i in range(n):
    list.append(int(input()))
sapxep(list)
print("Mảng đã được sắp xếp: ", list)

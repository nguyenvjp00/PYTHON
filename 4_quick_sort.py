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

list = []
print("Nhập vào số phần tử của mảng: ")
n = int(input())
print("Nhập vào các phần tử của mảng: ")
for i in range(n):
    list.append(int(input()))
sort(list)
print("Mảng đã được sắp xếp: ", list)
def sapxep(list):
    in_length = range(1, len(list))
    for i in in_length:
        to_sort = list[i]
        while list[i - 1] > to_sort and i > 0:
            list[i], list[i - 1] = list[i - 1], list[i]
            i = i - 1
    return list


list = []
print("Nhập vào số phần tử của mảng: ")
n = int(input())
print("Nhập vào các phần tử của mảng: ")
for i in range(n):
    list.append(int(input()))
sapxep(list)
print("Mảng đã được sắp xếp: ", list)

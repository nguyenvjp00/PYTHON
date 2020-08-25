def sapxep(list):
    in_length = len(list) - 1
    for i in range(in_length):
        min_value = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_value]:
                min_value = j
        if min_value != i:
            list[min_value], list[i] = list[i], list[min_value]
    return list


list = []
print("Nhập vào số phần tử của mảng: ")
n = int(input())
print("Nhập vào các phần tử của mảng: ")
for i in range(n):
    list.append(int(input()))
sapxep(list)
print("Mảng đã được sắp xếp: ", list)

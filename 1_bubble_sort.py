def sapxep(list):
    in_length = len(list) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, in_length):
            if list[i] > list[i + 1]:
                sorted = False
                list[i], list[i + 1] = list[i + 1], list[i]
    return list


list = []
print("Nhập vào số phần tử của mảng: ")
n = int(input())
print("Nhập vào các phần tử của mảng: ")
for i in range(n):
    list.append(int(input()))
sapxep(list)
print("Mảng đã được sắp xếp: ", list)

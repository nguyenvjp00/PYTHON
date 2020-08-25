def sapxep(list):
    in_length = len(list) - 1
    for i in range(in_length):
        for j in range(0, in_length - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


list = []
print("Nhập vào số phần tử của mảng: ")
n = int(input())
print("Nhập vào các phần tử của mảng: ")
for i in range(n):
    list.append(int(input()))
sapxep(list)
print("Mảng đã được sắp xếp: ", list)

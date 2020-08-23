def sort(list):
    for i in range(0, len(list) - 1):
        smallest = i
        for j in range(i + 1, len(list)):
            if list[j] < list[smallest]:
                smallest = j
        list[i], list[smallest] = list[smallest], list[i]

    return list

list = []
print("Nhập vào số phần tử của mảng: ")
n = int(input())
print("Nhập vào các phần tử của mảng: ")
for i in range(n):
    list.append(int(input()))
sort(list)
print("Mảng đã được sắp xếp: ", list)
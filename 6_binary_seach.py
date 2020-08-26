def binary_search(list, n):
    begin_index = 0
    end_index = len(list) - 1

    while begin_index <= end_index:
        midpoint = (begin_index + end_index) // 2
        if list[midpoint] == n:
            return True
        elif list[midpoint] < n:
            begin_index = midpoint + 1
        else:
            end_index = midpoint - 1


list = [7, 1, 8, 5, 6, 3, 9, 2, 4, 10]
print("Mảng được sắp xếp: ", sorted(list))
n = 8
print("Số cần tìm: ", n)

if binary_search(list, n):
    print("Tìm thấy tại vị trí số: ", n)
else:
    print("Không tìm thấy")

pos = -1


def linear_search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1
    return False


list = [6, 9, 2, 1, 8, 4, 3, 7, 5]
print("Mảng truyền vào: ", list)
n = 3
print("Số cần tìm: ", n)

if linear_search(list, n):
    print("Tìm thấy tại vị trí số: ", pos + 1)
else:
    print("Không tìm thấy")

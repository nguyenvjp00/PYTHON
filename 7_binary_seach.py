# pos = -1


def binary_search(list, n):
    begin_index = 0
    end_index = len(list) - 1

    while begin_index <= end_index:
        midpoint = (begin_index + end_index) // 2
        if list[midpoint] == n:
            #globals()['pos'] = midpoint
            return True
        elif list[midpoint] < n:
            begin_index = midpoint + 1
        else:
            end_index = midpoint - 1


def bubble_sort(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp


list = [7, 1, 8, 5, 6, 3, 9, 2, 4, 10]
bubble_sort(list)
print(list)
n = 8

if binary_search(list, n):
    print("Found", n)
else:
    print("Not found")

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
n = 10

if linear_search(list, n):
    print("Found at", pos + 1)
else:
    print("Not found")

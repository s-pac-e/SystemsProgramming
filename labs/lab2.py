
#####Branden Sauceda#####

pos = 0

n = 0

def search(array, n):
    l = 0
    u = len(array) - 1
    while l <= u:
        mid = (l + u) // 2
        if array[mid] == n:
            globals()['pos'] = mid
            return n
        elif array[mid] < n:
            l = mid + 1
        else:
            u = mid - 1
    return pos+1

array = [n for n in range(10)]

print(search(array, 3))
print(search(array, 7))
print(search(array, 11))
print(search(array, 20))

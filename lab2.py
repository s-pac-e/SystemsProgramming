
#####Branden Sauceda#####

pos = -1

def search(list, n):
    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        elif list[mid] < n:
            l = mid + 1
        else:
            u = mid - 1
    return False

list = [1, 2, 3, 4, 5, 7, 8, 9, 10, 15, 25, 50, 100, 200, 400, 800, 1000]
n = 25

if search(list, n):
    print(n,"Found at", pos + 1)
else:
    print("Number",n, "Not Found")

def binary_search(arr, target):
    arr.sort()  
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None  

li = [3,2,4,65,3]
print(binary_search(li,65))
def quick_sort(list1):
    if len(list1) <= 1:
        return list1
    else:
        pivot = list1[0]
        lesser = [x for x in list1[1:] if x <= pivot]
        greater = [x for x in list1[1:] if x > pivot]
        return quick_sort(lesser)+[pivot]+quick_sort(greater)
mylist = [4,3,1,5,3,2]
mylist = quick_sort(mylist)
print(mylist)
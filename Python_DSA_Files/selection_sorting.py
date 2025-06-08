def selection_sort(list1):
    n = len(list1)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if list1[j] < list1[min_index]:
                min_index = j
            list1[i],list1[min_index] = list1[min_index],list1[i]
    print(list1)

li = [2,4,1,1,32,4]
selection_sort(li)
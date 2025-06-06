def datalist():
    my_list = [1,4,2,1,5]
    n = len(my_list)
    for i in range(n):
        for j in range(0,n-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
    print(my_list)
datalist()
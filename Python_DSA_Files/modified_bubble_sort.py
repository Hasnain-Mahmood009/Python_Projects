def datalist(my_list):
    flag = False
    n = len(my_list)
    for i in range(n):
        flag = False
        for j in range(0,n-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
                flag = True
            if not flag:
                break
    print(my_list)

li = [2,4,2,1,3,5]
datalist(li)
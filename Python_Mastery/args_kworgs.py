# *args is a technique in Python that allows us to pass multiple arguments to a function without 
# specifying the exact number. These arguments are converted into a tuple inside the function. In the 
# parameter list, we can use any name after the *, but as good programmers, we typically use the name args.

# ------------------------------------------------------------------------------------------------------------------------>

def fun(*args):
    for item in args:
        print(f"this is item : {item}")
fun(1,2,3,"Example")

# ------------------------------------------------------------------------------------------------------------------------>

#  Q1: Write a function that multiplies all numbers given to it.
def multiplies_num(*args):
    print(sum(args))
multiplies_num(1,2,3,4)

# ------------------------------------------------------------------------------------------------------------------------>

# Q2: Write a function that returns the maximum number from the given arguments.
def max_num(*args):
    print(max(args))
max_num(1,2,3,24,1,2)

#------------------------------------------------------------------------------------------------------------------------->
#  Q3: Write a function that sums only the even numbers from the arguments.
def sum_even(*args):
    li = []
    for num in args:
        if num % 2 == 0:
            li.append(num)
    print(sum(li))
sum_even(1, 2, 3, 4, 5)


#------------------------------------------------------------------------------------------------------------------------->
#                                                      --Kwargs--                                                         #
#------------------------------------------------------------------------------------------------------------------------->
# kwargs is similar to args, but there is one main difference: args converts all values 
# into a tuple, whereas kwargs converts them into a dictionary

def fun(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
fun(name="Hasnain", age = "16")

# Write a function that prints student details like name, class, age, etc.
def stu_detial(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
stu_detial(name="Hasnain", class_ = "10th", roll_no = "4")

# Write a function that counts how many keyword arguments were passed.
def count_keyword(**kwargs):
    print(f"Total keyword arguments : {len(kwargs)}")
count_keyword(name = "Hasnain", age = "16" , gender = "Male")

# Write a function that returns all keyword argument keys as a list.
def keyword_To_list(**kwargs):
    li = []
    for key,value in kwargs.items():
        li.append(key)
    print(li)
keyword_To_list(name = "Hasnain", age = "16" , gender = "Male")

# Write a function that prints all positional arguments first, then all keyword arguments.
def fun(*args,**kwargs):
    li = []
    for item in args:
        li.append(item)
    for key,value in kwargs.items():
        x = f"{key} : {value}"
        li.append(x)
    print(li)
fun(1,2,3, name = "Hasnain", age = "16")
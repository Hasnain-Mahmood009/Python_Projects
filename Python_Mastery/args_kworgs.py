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

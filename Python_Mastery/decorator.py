def decorat(func):
    def wrapper(name):
        print("Hellow")
        func(name)
        print("How are you")
    return wrapper

@decorat
def func(name):
    print(name)

func("Hasnain")

# <<--------------------------------------------------------------------------------------------------------------------->>

# Q1.Write a decorator that prints "Function is being called" before the function runs, 
# and "Function call completed" after the function finishes.
def decorat_func(func):
    def wrapper(arg):
        print("Function is being called")
        func(arg)
        print("Function call completed")
    return wrapper

@decorat_func
def func(arg):
    print(arg)

func("function is calling...")

# <<--------------------------------------------------------------------------------------------------------------------->>

# Q2. Write a decorator that calls the decorated function twice every time it's used.
def func(arg):
    def wrapper(argu):
        arg(argu)
        arg(argu)
    return wrapper

@func
def funct(argu):
    print(argu)
funct("Hellow world")

# <<--------------------------------------------------------------------------------------------------------------------->>

# Write a decorator that checks whether the decorated function received any arguments:
# If no arguments, print "No arguments passed!"
# If arguments are passed, print "Arguments passed"
def func(fun):
    def wrapper(*args):
        if len(args) == 0:
            print("No arguments passed!")
        else:
            print("Arguments passed..")
    return wrapper

@func
def fun(args):
    print(args)

fun(34)
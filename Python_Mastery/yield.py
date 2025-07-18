# In Python, yield is a keyword used inside functions to create generators. Unlike return, which ends the function, 
# yield pauses the function and saves its state, allowing it to continue from the same point later. This is 
# especially useful when you want to return a large sequence of values one at a time, without using too much memory. 
# Each time the generator is called (like in a for loop), it resumes where it left off and gives the next 
# value. Using yield is ideal when you want to loop through big data or create custom iterators efficiently.

def even_generator(limit):
    for i in range(2,limit,2):
        yield i
for nums in even_generator(10):
    print(nums)

# <<-------------------------------------------------------------------------------------------------------------------------->>

# Fibonacci Sequence Generator
def febonacci(n):    
    a,b = 1,0
    while a <=n:
        yield b
        a,b = b,a+b
for i in febonacci(13):
    print(i,end=" ")

# <<-------------------------------------------------------------------------------------------------------------------------->>

# Countdown Generator
def countDown(n):
    for i in range(10,0,-1):
        yield i
for i in countDown(10):
    print(i)

# <<-------------------------------------------------------------------------------------------------------------------------->>

# Infinite Prime Number Generator
def prime_number(n):
    for i in range(2,n):
        if n <= 1:
            yield "Not Prime"
        if n%i == 0:
            yield "Not prime"
            break
        else:
            yield "prime"
            break
for i in prime_number(9):
    print(i)
def sum(n):
    if n == 1:
        return 1
    else:
        s = n + sum(n-1)
        return s
print(sum(5),"\n")

def odd(n):
    if n == 1:
        return 1
    else:
        s = 2*n-1 + odd(n-1)
        return s
        
print("Odd")
print(odd(10))

def even(n):
    if n == 1:
        return 2
    else:
        s = 2*n + even(n-1)
        return s
        
print("even")
print(even(10))

def fact(n):
    if n == 1:
        return 2
    else:
        s = n * fact(n-1)
        return s
        
print("fact")
print(fact(1000))

def square(n):
    if n == 1:
        return 2
    else:
        s = n*n + square(n-1)
        return s
        
print("square")
print(square(10))
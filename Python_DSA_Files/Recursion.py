def printN(n):
    if n > 0:
        printN(n - 1)
        print(n, end=" ")
printN(5)

def printNreverse(n):
    if n > 0:
        print(n,end=" ")
        printNreverse(n - 1)
print()
printNreverse(5)

def even(n):
    if n > 0:
        even(n - 1)
        if n %2 == 0:
            print(n,end=" ")
print("\n Even")
even(10)

def odd(n):
    if n > 0:
        odd(n - 1)
        if n %2 != 0:
            print(n, end=" ")
print("\n Odd")
odd(10)

def evenReverse(n):
    if n > 0:
        if n %2 == 0:
            print(n, end=" ")
        evenReverse(n - 1)
print("\n Even number in reverse order...")
evenReverse(10)

def odd(n):
    if n > 0:
        if n %2 != 0:
            print(n, end=" ")
        odd(n - 1)
print("\n Odd number in reverse order...")
odd(10)
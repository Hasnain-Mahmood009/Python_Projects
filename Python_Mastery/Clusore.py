def outer():
    def inner(name):
        print(f"Hellow {name}")
    return inner
outer_func = outer()
outer_func("Hasnain")
def Gen():
    n = 1
    print("Yield 1")
    yield n

    n = 2
    print("Yield 2")
    yield

    n = 3
    print("Yield 3")
    yield

# Way 1 : next
a = Gen()
next(a)
next(a)
next(a)

#Way 2 : interator
#for item in Gen():
#    print(item)

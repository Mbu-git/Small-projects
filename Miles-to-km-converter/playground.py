def add(*n):
    total = 0
    for number in n:
        total += number
    return total

def calculate(n,**kwargs):
    print(kwargs)
    # Since kwargs is a dictionary you can iterate through like:
    # for key, value in kwargs.items():
    #   print(key)
    #   print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]

calculate(add=3,multiply=5)

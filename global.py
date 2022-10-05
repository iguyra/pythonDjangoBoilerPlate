
""""we can only access global variables from a function,
to be able to modify it, we have to use the global keyword
"""

c = 1  # global variable


def add():
    global c
    c = c + 1
    print(c)


add()

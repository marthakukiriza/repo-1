def outer(x):
    def inner():
        nonlocal x
        x*2
        print("X - inner: ", x)
    print("X - outer: ", x)
    inner()

outer(2)


class Person:
    def __init__(self):
        pass

    def print_hello():
        print("Hello, I'm new to git")

    def auth(password):
        passkey = "hello230"
        does_match = password == passkey
        if does_match:
            print("Password Matches")
        else:
            print("Wrong password")
        return does_match            
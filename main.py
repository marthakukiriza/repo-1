def outer(x):
    def inner():
        nonlocal x
        x*2
        print("X - inner: ", x)
    print("X - outer: ", x)
    inner()

outer(2)
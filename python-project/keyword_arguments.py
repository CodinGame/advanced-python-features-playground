def f(*args, **kwargs):
    print("Arguments: ", args)
    print("Keyword arguments: ", kwargs)

f(3, 4, 9, foo=42, bar=7)

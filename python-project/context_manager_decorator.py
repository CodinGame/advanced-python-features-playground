from contextlib import contextmanager


@contextmanager
def colored_output(color):
    print("\033[%sm" % color, end="")
    yield
    print("\033[0m", end="")


print("Hello, World!")
with colored_output(31):
    print("Now in color!")
print("So cool.")

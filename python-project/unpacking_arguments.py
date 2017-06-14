def repeat(count, name):
    for i in range(count):
        print(name)

print("Call function repeat using a list of arguments:")
args = [4, "cats"]
repeat(*args)

print("Call function repeat using a dictionary of keyword arguments:")
args2 = {'count': 4, 'name': 'cats'}
repeat(**args2)

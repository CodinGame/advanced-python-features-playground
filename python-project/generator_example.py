a = (x * x for x in range(100))

# a is a generator object
print(type(a))

# Sum all the numbers of the generator
print(sum(a))

# There are no elements left in the generator
print(sum(a))

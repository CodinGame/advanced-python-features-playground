The source code is on [GitHub](https://github.com/CodinGame/python-template), please feel free to come up with proposals to improve it.

# Generators

A generator is an object that produces a sequence of values. It can be used as an iterator, which means that you can use it with a `for` statement, or use the `next` function to get the next value. However, you can iterate over the values only once.

A generator can be created using a function that uses the `yield` keyword to generate a value. When a generator function is called, a generator object is created.

@[yield operator]({"stubs": ["yield_example.py"], "command": "python3 yield_example.py"})

For simple cases, it is possible to create a generator using a generator expression. As opposed to a list, the values will be computed on the fly instead of being computed once and stored in memory.

@[generator expressions]({"stubs": ["generator_example.py"], "command": "python3 generator_example.py"})

# Collections

[`collections`](https://docs.python.org/3/library/collections.html) is a module in the standard library that implements alternative container datatypes.

For example, a [`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter) is a collection where elements are stored as dictonary keys and their counts are stored as dictionary values:

@[Counter]({ "stubs": ["collections_counter.py"], "command": "python3 collections_counter.py" })

A [`defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict) is a subclass of `dict`, which allows to pass a factory used to create automatically a new value when a key is missing.

@[defaultdict]({"stubs": ["defaultdict.py"], "command": "python3 defaultdict.py"})

The `defaultdict` can be used to create a tree data structure!

@[Tree]({"stubs": ["defaultdict_tree.py"], "command": "python3 defaultdict_tree.py"})

# Itertools

[`itertools`](https://docs.python.org/3/library/itertools.html) is a module in the standard library that allows you to to create iterators for efficient looping.

For example, [`permutations`](https://docs.python.org/3/library/itertools.html#itertools.permutations) ) allows you to generate all the possible ways of ordering a set of things:

@[permutations]({ "stubs": ["itertools_permutations.py"], "command": "python3 itertools_permutations.py" })

Similarly, [`combinations` ](https://docs.python.org/3/library/itertools.html#itertools.combinations) generates all the possible ways of selecting items from a collection, such that (unlike permutations) the order does not matter:

@[combinations]({ "stubs": ["itertools_combinations.py"], "command": "python3 itertools_combinations.py" })

`itertools` also contains utility functions such as `chain`, which takes iterables and creates a new iterator that returns elements from the given iterables sequentially, as a single sequence:

@[chain]({ "stubs": ["itertools_chain.py"], "command": "python3 itertools_chain.py" })

# Packing and Unpacking

The `*` operator, known as the unpack or splat operator allows very convenient transformations, going from list or tuples to separate variables or arguments and conversely.

@[Extended Iterable Unpacking]({"stubs": ["unpacking.py"], "command": "python3 unpacking.py"})

When the arguments for you function are already in a list of tuple, you can unpack them using `*args` if it's a `list`, or `**kwargs` if that's a `dict`.

@[unpacking arguments]({"stubs": ["unpacking_arguments.py"], "command": "python3 unpacking_arguments.py"})

The opposite is also possible, you can define a function that will pack all the arguments in a single list.

@[keyword arguments]({"stubs": ["keyword_arguments.py"], "command": "python3 keyword_arguments.py"})

# Decorators

A decorator is simply a function which takes a function as a parameter and returns a function. 

For example, in the following code, the `cache` function is used as a decorator to remember the Fibonacci numbers that have already been computed:

@[decorators]({ "stubs": ["decorators.py"], "command": "python3 decorators.py" })

The [`functools`](https://docs.python.org/3/library/functools.html) module provides a few decorators, such as [`lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache) which can do what we just did: memoization. It saves recent calls to same time when a given function is called with the same arguments:

@[lru_cache]({ "stubs": ["lru_cache.py"], "command": "python3 lru_cache.py" })

# Context Manager

Context managers are mainly used to properly manage ressources. The most common use of a context manager is the opening of a file: `with open('workfile', 'r') as f:`. But most developers have no idea how that really works underneath nor how they can create their own.

A [context manager](https://docs.python.org/3/library/stdtypes.html#typecontextmanager) is a class that implements the methods `__enter__` and `__exit__`.

@[Context Manager]({"stubs": ["context_manager.py"], "command": "python3 context_manager.py"})

For simple use cases, it's also possible to use a generator function with a single `yield`, using the `@contextmanager` decorator. [See the documentation.](https://docs.python.org/3/library/contextlib.html)

@[Context Manager Using @contextmanager]({"stubs": ["context_manager_decorator.py"], "command": "python3 context_manager_decorator.py"})

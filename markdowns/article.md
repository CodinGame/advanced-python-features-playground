The source code is on [GitHub](https://github.com/CodinGame/python-template), please feel free to come up with proposals to improve it.

# Generators

A generator is an object that produces a sequence of values. It can be used as an iterator, which means that you can use it with a `for` statement, or use the `next` function to get the next value. However, you can iterate over the values only once.

A generator can be created using a function that uses the `yield` keyword to generate a value. When a generator function is called, a generator object is created.

@[yield operator]({"stubs": ["yield_example.py"], "command": "python3 yield_example.py"})

For simple cases, it is possible to create a generator using a generator expression. As opposed to a list, the values will be computed on the fly instead of being computed once and stored in memory.

@[generator expressions]({"stubs": ["generator_example.py"], "command": "python3 generator_example.py"})

# Collections

@[Counter]({ "stubs": ["collections_counter.py"], "command": "python3 collections_counter.py" })

@[defaultdict]({"stubs": ["defaultdict.py"], "command": "python3 defaultdict.py"})

@[Tree]({"stubs": ["defaultdict_tree.py"], "command": "python3 defaultdict_tree.py"})

# Itertools

`itertools` is a module in the standard library that allows you to to create iterators for efficient looping.

For example, [`permutations`](https://docs.python.org/3/library/itertools.html#itertools.permutations) ) allows you to generate all the possible ways of ordering a set of things:

@[permutations]({ "stubs": ["itertools_permutations.py"], "command": "python3 itertools_permutations.py" })

Similarly, [`combinations` ](https://docs.python.org/3/library/itertools.html#itertools.combinations) generates all the possible ways of selecting items from a collection, such that (unlike permutations) the order does not matter:

@[combinations]({ "stubs": ["itertools_combinations.py"], "command": "python3 itertools_combinations.py" })

`itertools` also contains utility functions such as `chain`, which takes iterables and creates a new iterator that returns elements from the given iterables sequentially, as a single sequence:

@[chain]({ "stubs": ["itertools_chain.py"], "command": "python3 itertools_chain.py" })

# Unpacking

@[Extended Iterable Unpacking]({"stubs": ["unpacking.py"], "command": "python3 unpacking.py"})

@[unpacking arguments]({"stubs": ["unpacking_arguments.py"], "command": "python3 unpacking_arguments.py"})

@[keyword arguments]({"stubs": ["keyword_arguments.py"], "command": "python3 keyword_arguments.py"})

# Decorators

@[decorators]({ "stubs": ["decorators.py"], "command": "python3 decorators.py" })

@[lru_cache]({ "stubs": ["lru_cache.py"], "command": "python3 lru_cache.py" })

# Context Manager

@[Context Manager]({"stubs": ["context_manager.py"], "command": "python3 context_manager.py"})

@[Context Manager Using @contextmanager]({"stubs": ["context_manager_decorator.py"], "command": "python3 context_manager_decorator.py"})

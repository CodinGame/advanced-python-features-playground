from collections import defaultdict

my_dict = defaultdict(lambda: 'Default Value')
my_dict['a'] = 42

print(my_dict['a'])
print(my_dict['b'])

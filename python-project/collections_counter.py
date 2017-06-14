from collections import Counter

a = Counter('blue')
b = Counter('yellow')

print(a)
print(b)
print((a + b).most_common(3))

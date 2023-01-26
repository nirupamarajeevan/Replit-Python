# squaring and sorting a given list using lambda expressions
my_list = [5, 4, 3]
# Squaring
print(list(map(lambda item: item * item, my_list)))


# Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key = lambda x: x[1])
print(a)

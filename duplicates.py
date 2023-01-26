# checking duplicates in a given list using list comprehension
my_list = ['a', 'v', 'p', 'o', 'n', 'p', 'm', 'n']
duplicates = list(set(x for x in my_list if my_list.count(x) > 1))
print(duplicates)

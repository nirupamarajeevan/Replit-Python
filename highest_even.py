# printing the highest even number from a given list
def highest_even(*li):
  # li = int(input("Enter a list of numbers"))
  even = []
  for i in li:
    if i % 2 == 0:
      even.append(i)
  high_even = max(even)
  print(high_even)

highest_even(12, 3, 6, 1, 8, 10)

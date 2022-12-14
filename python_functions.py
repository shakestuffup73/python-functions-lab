
#! sum_to

def sum_to(n):
  total = 0
  sum = 0
  while total <= n:
    total += 1
    sum += total
  return sum

print(sum_to(55))

#! largest

def largest(list):
  list.sort()
  return list[-1]

print(largest([10, 4, 3, 213, 91]))


#! occurrences

def occurrences(str1, str2):
  return str1.count(str2)

print(occurrences('feep', 'e'))
print(occurrences('bananananana', 'a'))


#! product

def product(*args):
  sum = 1
  for arg in args:
    sum *= arg
  return sum

print(product(2, 2, 2))
print(product(1, 3, 4))
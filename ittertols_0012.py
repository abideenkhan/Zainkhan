# -*- coding: utf-8 -*-
"""ittertols-0012.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KBknxvyOAsoZycLm36fbXzNg0YwKzGvh

## ***The IterTools module***
The itertools module contains a number of commonly used iterators as well as functions for combining several iterators.

The module’s functions fall into a few broad classes:
•	Functions that create a new iterator based on an existing iterator.

•	Functions for treating an iterator’s elements as function arguments.

•	Functions for selecting portions of an iterator’s output.

•	A function for grouping an iterator’s output
"""

from itertools import count

for number in count(start=1, step=2):
	if number > 10:
		break
	print(number)

"""## ***Infinite Iterators***

"""

import itertools
for i in itertools.count(5, 5):
	if i == 35:
		break
	else:
		print(i, end=" ")

"""# ***2. cycle(iterable):***"""

import itertools

count = 0


for i in itertools.cycle('AB'):
	if count > 7:
		break
	else:
		print(i, end=" ")
		count += 1

import itertools

l = ['CSE', 'COM', 'ECM']

iterators = itertools.cycle(l)


for i in range(6):

	print(next(iterators), end=" ")

import itertools

print("Printing the numbers repeatedly : ")
print(list(itertools.repeat(25, 4)))

"""# ***2. Combinatoric iterators***"""

from itertools import product

print("The cartesian product using repeat:")
print(list(product([1, 2], repeat=2)))
print()

print("The cartesian product of the containers:")
print(list(product(['COM', 'CSE', 'ECM'], '2')))
print()

print("The cartesian product of the containers:")
print(list(product('AB', [3, 4])))

"""# ***Permutations():***

"""

from itertools import permutations

print("All the permutations of the given list is:")
print(list(permutations([1, 'Computer'], 2)))
print()

print("All the permutations of the given string is:")
print(list(permutations('AB')))
print()

print("All the permutations of the given container is:")
print(list(permutations(range(3), 2)))

"""# ***Combinations(): ***

"""

from itertools import combinations

print ("All the combination of list in sorted order(without replacement) is:")
print(list(combinations(['A', 2], 2)))
print()

print ("All the combination of string in sorted order(without replacement) is:")
print(list(combinations('AB', 2)))
print()

print ("All the combination of list in sorted order(without replacement) is:")
print(list(combinations(range(2), 1)))

"""# ***Combinations_with_replacement(): ***"""

from itertools import combinations_with_replacement

print("All the combination of string in sorted order(with replacement) is:")
print(list(combinations_with_replacement("AB", 2)))
print()

print("All the combination of list in sorted order(with replacement) is:")
print(list(combinations_with_replacement([1, 2], 2)))
print()

print("All the combination of container in sorted order(with replacement) is:")
print(list(combinations_with_replacement(range(2), 1)))

"""# **Terminating iterators**

"""

import itertools
import operator

li1 = [1, 4, 5, 7]

print("The sum after each iteration is : ", end="")
print(list(itertools.accumulate(li1)))

print("The product after each iteration is : ", end="")
print(list(itertools.accumulate(li1, operator.mul)))


print("The sum after each iteration is : ", end="")
print(list(itertools.accumulate(li1)))

print("The product after each iteration is : ", end="")
print(list(itertools.accumulate(li1, operator.mul)))

"""## 2.**chain(iter1, iter2..):**"""

import itertools

li1 = [1, 4, 5, 7]

li2 = [1, 6, 5, 9]

li3 = [8, 10, 5, 4]
print("All values in mentioned chain are : ", end="")
print(list(itertools.chain(li1, li2, li3)))

"""# 3.***chain.from_iterable():***"""

import itertools


li1 = [1, 4, 5, 7]
li2 = [1, 6, 5, 9]


li3 = [8, 10, 5, 4]

li4 = [li1, li2, li3]

print ("All values in mentioned chain are : ", end ="")
print (list(itertools.chain.from_iterable(li4)))

"""# 4. ***compress(iter, selector):***"""

import itertools

print("The compressed values in string are : ", end="")
print(list(itertools.compress('GEEKSFORGEEKS', [
	1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0])))

"""5.***dropwhile(func, seq):***"""

import itertools


li = [2, 4, 5, 7, 8]


print ("The values after condition returns false : ", end ="")
print (list(itertools.dropwhile(lambda x : x % 2 == 0, li)))

"""6. # ***dropwhile(func, seq):***"""

import itertools


li = [2, 4, 5, 7, 8]

print ("The values after condition returns false : ", end ="")
print (list(itertools.dropwhile(lambda x : x % 2 == 0, li)))

"""##7.  ***filterfalse(func, seq):***"""

import itertools
li = [2, 4, 5, 7, 8]
print ("The values that return false to function are : ", end ="")
print (list(itertools.filterfalse(lambda x : x % 2 == 0, li)))

"""# 8.***islice(iterable, start, stop, step):***

"""

import itertools


li = [2, 4, 5, 7, 8, 10, 20]

print ("The sliced list values are : ", end ="")
print (list(itertools.islice(li, 1, 6, 2)))

"""# 9.***starmap(func., tuple list):***

"""

import itertools


li = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1) ]

print ("The values acc. to function are : ", end ="")
print (list(itertools.starmap(min, li)))

"""# 10. ***takewhile(func, iterable):***"""

import itertools

li = [2, 4, 6, 7, 8, 10, 20]

print ("The list values till 1st false value are : ", end ="")
print (list(itertools.takewhile(lambda x : x % 2 == 0, li )))

"""##11 ***tee(iterator, count):- ***This iterator splits the container into a number of iterators mentioned in the argument."""

import itertools

li = [2, 4, 6, 7, 8, 10, 20]


iti = iter(li)

it = itertools.tee(iti, 3)

print("The iterators are : ")
for i in range(0, 3):
	print(list(it[i]))

"""#12 ***zip_longest( iterable1, iterable2, fillval):***

"""

import itertools
print("The combined values of iterables is : ")
print(*(itertools.zip_longest('Peiec', 'rsdny', fillvalue='_')))
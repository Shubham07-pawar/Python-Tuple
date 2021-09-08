# Write a Python program calculate the product, multiplying all the numbers of a given tuple.
# Original Tuple:
# (4, 3, 2, 2, -1, 18)
# Product - multiplying all the numbers of the said tuple: -864
# Original Tuple:
"""
# using for loop

t1 = (4, 3, 2, 2, -1, 18)
product = 1
for i in t1:
    product *= i
print(f"multiplying all the numbers of tuple is {product}")
----------------------------------------------------------------------------------------------------------------------------

# using while loop
t1 = (4, 3, 2, 2, -1, 18)
product = 1
s = 0
while s < len(t1):
    product *= t1[s]
    s += 1
print(f"multiplying all the numbers of tuple is {product}")
------------------------------------------------------------------------------------------------------------------------------

# using lambda function
from functools import reduce as rd
t1 = (4, 3, 2, 2, -1, 18)
s = rd(lambda x, y: x * y, t1)
print(f"multiplying all the numbers of tuple is {s}")

---------------------------------------------------------------------------------------------------------------------------
"""
# using tuple comprehension
from functools import reduce as rd

t1 = (4, 3, 2, 2, -1, 18)

t2 = (rd(lambda x, y: x * y, t1))
print(t2)

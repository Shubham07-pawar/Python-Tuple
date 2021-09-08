# Write a Python program to add an item in a tuple
# Using for loop
"""
t1 = (10, 20, 30, 40, 50)
t2 = []
for i in t1:
    t2.append(i)
t2.append(60)
print(tuple(t2))
------------------------------------------------------------------------------------------------------------------------

# using while loop
t1 = (10, 20, 30, 40, 50)
t2 = []
s = 0
while s < len(t1):
    t2.append(t1[s])
    s += 1
t2.append(70)
print(tuple(t2))
----------------------------------------------------------------------------------------------------------------------------

# list comprehension
t1 = (10, 20, 30, 40, 50)
t2 = [x for x in t1]
t2.append(60)
print(tuple(t2))
------------------------------------------------------------------------------------------------------------------------------
"""
# using merge of tuples with the + operator you can add an element and it will create a new tuple
t1 = (10, 20, 30, 40, 50)
t1 = t1 + (60,)
print(t1)
# if you want to add element in between of tuple
t1 = t1[:5] + (70, 80, 90) + t1[5:]
print(t1)


#  Write a Python program to remove an item from a tuple
t1 = (10, 20, 30, 40, 50, 55, 60)
l1 = list(t1)  # convert tuple to list
l1.pop(-2)  # list pop method
l1.remove(60) # list remove method
print(tuple(l1))

# another way
t1 = (10, 20, 30, 40, 50, 55, 60)
t1 = t1[:3] + t1[4:] # remove 40 using slicing
print(t1)





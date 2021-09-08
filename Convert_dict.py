# Write a Python program to convert a tuple to a dictionary.
t1 = (10, 20, 30, 40, 50, 55, 60)
d1 = {}
for i in t1:
    d1[i] = i
print(d1)
# another way
# create a tuple
tuplex = ((2, "w"), (3, "r"))
print(dict((y, x) for x, y in tuplex))


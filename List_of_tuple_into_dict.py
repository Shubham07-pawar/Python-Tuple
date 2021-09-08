# Write a Python program to convert a list of tuples into a dictionary
t1 = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d = {}
for a,b in t1:
    d.setdefault(a,[]).append(b)
print(d)









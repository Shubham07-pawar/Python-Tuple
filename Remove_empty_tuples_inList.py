# Write a Python program to remove an empty tuple(s) from a list of tuples. Go to the editor
# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
l1 = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
l2 = []
for i in l1:
    if i == ():
        pass
    else:
        l2.append(i)
print(l2)

# list comprehension
l1 = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
l2 = [x for x in l1 if x]
print(l2)




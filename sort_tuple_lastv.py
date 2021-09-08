# Write a Python program to sort a tuple by its float element.
# Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
def last(n):
    return n[-1]


def sort_1(tuples):
    return sorted(tuples, key=last,reverse=True)


l1 = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(sort_1(l1))


# using lambda function
l1 = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
l2 = sorted(l1, key= lambda x: float(x[-1]), reverse=True)
print(l2)

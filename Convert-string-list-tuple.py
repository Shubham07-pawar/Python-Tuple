#  Write a Python program convert a given string list to a tuple.
# Original string: python 3.0
# Convert the said string to a tuple:
# ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')

s1 = "python 3.0"
l1 = []
for i in s1:
    l1.append(i)
print(tuple(l1))

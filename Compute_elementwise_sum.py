# n Write a Python program to compute element-wise sum of given tuples.
s = [(1, 2, 3, 4), (4, 2, 1, 3), (5, 6, 2, 1), (2, 5, 2, 1)]
s1 = []
for i in range(0, 4):
    s2 = s[0][i] + s[1][i] + s[2][i] + s[3][i]
    s1.append(s2)
print(tuple(s1))

# another way
s2 = tuple(map(sum, zip(*s)))
print(s2)

# . Write a Python program to convert a given tuple of positive integers into an integer.
# Original tuple:
# (1, 2, 3)
# Convert the said tuple of positive integers into an integer:
# 123

t1 = (1, 2, 3)
s1 = ''
for i in t1:
    s1 += str(i)
print(int(s1))

# another way
t1 = (1, 2, 3, 5, 5, 6)
t2 = str(t1)
s1 = "".join(t2).replace(", ", "")
print(s1[1:len(s1)-1])

# another way
t1 = (1, 2, 3)
print(int(''.join(map(str, t1))))


#  Write a Python program to convert a tuple of string values to a tuple of integer values. Go to the editor
# Original tuple values:
# (('333', '33'), ('1416', '55'))
# New tuple values:
# ((333, 33), (1416, 55))

t1 = (('333', '33'), ('1416', '55'))
t2 = tuple((int(x[0]), int(x[1])) for x in t1)
print(t2)

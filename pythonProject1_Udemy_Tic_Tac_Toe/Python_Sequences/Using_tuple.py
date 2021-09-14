t1 = (1, 2, 3, 4.12, 'string', True)
# tuples are immutable(Can't delete, assign new value, add new value)
# del t1[0]
# t1.append('string')
# t1[3] = True
print(t1)
print(len(t1))
# Tuple join
t2 = ('adya', 20)
t3 = t1 + t2
print(t3)
t4 = t2 * 2
print(t4)
print('string' in t1)
print(4.12 not in t1)
# TUPLE UNPACKING
a, b = t2
print(a)
print(b)

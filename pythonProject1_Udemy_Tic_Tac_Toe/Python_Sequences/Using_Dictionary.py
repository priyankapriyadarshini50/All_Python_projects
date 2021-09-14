d1 = {'cat': 'chat', 'dog': 'chein', 'horse': 'cheval'}
# LENGTH OF DICTIONARY
print(len(d1))
# DICTIONARIES ARE MUTABLE
d1['swan'] = 'cygne'
print(d1)
# Modify the dictionary
d1['swan'] = 'Cygne'
print(d1)
# Using Update and it does not return any dictionary, it just updates the same dictionary
d1.update({"duck":"canard"})
print(d1)
print()
# Dictionary is not iterable
# USING KEYS() METHOD: RETURNS AN ITERABLE OBJECT OF KEYS
print("The iterable object: ", d1.keys())
print(type(d1.keys()))
for key in d1.keys():
    print(key, "->", d1[key])
print()
# USING ITEM() METHOD: RETURNS AN ITERABLE OBJECT OF ITEM(KEY/VALUE) PAIR
for item in d1.items():
    print(item)
    c, d = item
    print(c, "->", d)
print()
# USING VALUES(): RETURNS AN ITERABLE OBJECT OF VALUES
for value in d1.values():
    print(value)
print("\n")
# SORTED METHOD SHORT THE DICTIONARY KEYS() and returns a new list each element is the key
d2 = sorted(d1)
print(d2)
print(sorted(d1.keys()))
print()
# SHOWs KeyError
# print(d1['elephant'])
# USING IN AND NOT IN OPERATOR
print('cat' in d1)
print("dog" not in d1)
print('chat' in d1)  # does not take values
# USING popitem(): it just delete the last item from the dictionary and does not return any value
d1.popitem()
print(d1)
# Using del keyword
del d1["dog"]
print(d1)
print()

# CONVERT A TUPLE INTO DICTIONARY
t3 = (('A',100), ('B', 200))
d3 = dict(t3)
print(d3)

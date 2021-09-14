from collections import Counter
my_tuple =(1, 2, 3, 1, 4, 4, 4, 'a', 'a')
res_dictionary = Counter(my_tuple)
print(res_dictionary)
print(type(res_dictionary))
# access the number of times 4 element occur
print(res_dictionary[4])
# applicable to string
s = 'aaabbbbccccdddggghh'
print(Counter(s))
# create an Counter object
c = Counter(s)
# return the most common occurrences
print(c.most_common(2))
# convert to a list of (elem, cnt) pairs
print(c.items())
# counter with words in sentence
sen = 'The name of the city is Melbourne'
s1 = sen.lower().split()
print(s1)
print(Counter(s1))
print(Counter(s1).most_common(1))


from collections import defaultdict
#d = {}
#print(d['a']) # shows KeyError
# create a defaultdict d with lambda 0
# whenever there is a wrong/invalid key, the default value would be 0
d = defaultdict(lambda:0.5)
d['correct'] = 100
d['a'] = 65
d['wrong key']
d['one']
for key in d:
    print(key, ':', d[key])
# namedtuple
from collections import namedtuple
Dog = namedtuple('Dog', ['Age', 'breed', 'name'])
sam = Dog(Age=5, breed='Lab', name='Sammy')  # tuple object/tuple
hush = Dog(3, 'Huskies', 'Tom')  # tuple object/tuple
print(sam)
print(sam.breed)  # either we can use the name to get the value
print(sam[1])  # or we can use the index number to get the value in the tuple
for item in hush:
    print(item)


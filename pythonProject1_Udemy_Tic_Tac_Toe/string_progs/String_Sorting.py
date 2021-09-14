# Sort a string
letters = 'yxzz'
new_lt = sorted(letters)
print(new_lt)
new_str = ''.join(new_lt)
print(new_str)
print()

# Another way to sort the string
my_list = list(letters)
print(my_list)
my_list.sort()
print(my_list)
sorted_str = ''.join(my_list)
print(sorted_str)
print()

# Sort a list which has string as each element
st_list = ['Bob', 'Alice', 'Adya']
st_list.sort()  # just update the current list
print(st_list)

new_lt = sorted(st_list)  # here it returns a new string
print(new_lt)


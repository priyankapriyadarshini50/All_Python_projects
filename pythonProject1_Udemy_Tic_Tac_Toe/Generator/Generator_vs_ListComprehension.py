the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
# Using parenthesis the generator is created
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

print(the_list)
print(the_generator)

for v in the_generator:
    print(v, end=' ')

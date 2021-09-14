# \ is used as a string
def str_length():
    i_am = 'I\n'
    count = 0
    for i in i_am:
        print('char: {}'.format(i))
        count += 1
    print(len(i_am))
    print(count)


str_length()

# The newline character is invisible
my_str = '''Line #1
Line #2'''  # 14 characters counting
print(len(my_str))

# get the ASCII code of a single character string
print(ord('a'))
print(chr(65))
print(chr(ord('A')) == 'A')

# Negative indexing
my_str1 = 'abcd'
for i in range(-4, 0):
    print(my_str1[i], end=' ')
print('\n')

# to keep the phrase/word at the center
print('['+'alpha'.center(9)+']')


def check_alpha_numeric():
    print('lambda30'.isalnum())
    print('30'.isalnum())
    print('lambda 30'.isalnum())  # it contains white spaces
    print('@#$'.isalnum())


check_alpha_numeric()

# checks for whitespace
print(' '.isspace())
print(' \n '.isspace())  # escape characters consider as spaces in a string
print("check for isspace")
print('\n\r\t '.isspace())

# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w"))
print("pythoninstitute.org".lstrip("python"))
print("aaaaabbbbcccc".lstrip("ab"))

# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("Apple juice".replace(" ", "*"))
print("This is it!".replace("is","are", 3))

# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))  # if the given string not in the actual string,it returns -1
print("tau tau tau".rfind("ta", 3, 9))

# Demonstrating the split() method:
print("phi       chi\npsi".split())
print("My,name is, Adya!".split(','))
print("My name is Adya!".split('a'))

# Demonstrating the startswith() method:
print("omega".startswith("meg"))
print("omega".startswith("om"))

# Demonstrating the strip() method:
print("[" + "   alpha   ".strip() + "]")
print("[" + "alpha".strip('a') + "]")

# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())

# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())

# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())


def mysplit(my_string):
    my_list = []
    word = ''
    str_lt = my_string.split(',')
    print(str_lt)
    inward = str_lt[0][0].isspace() != ' '
    print(inward)
    for char in my_string:
        if inward:  # The first character is not a space
            if char == ' ':
                my_list.append(word)
                word = ''

            else:
                word = word + char
            return my_list


print(mysplit("To be or not to be, that is the question"))
#print(mysplit("To be or not to be,that is the question"))
#print(mysplit("   "))
#print(mysplit(" abc "))
#print(mysplit(""))
print('11' < '8')
print("AB" < "Ab")
print("abcd" > "abc")
s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
print(s2)
s3 = sorted(s2)
print(s3)
print(s3[1])

s1 = '12'
i = int(s1)
print(i)
s2 = str(12.8)
f = float(s2)
print(f)
print(s1 == s2)

s3 = 'abcdA'
print(max(s3))
print(min(s3))

names = ['Alice', 'Bob', 'Charlie']
names.sort(key=lambda x: (x[-1], x[-2]), reverse=True)
print(names)
print("-----------------------")
print('ABc' > 'CAB')
print('99' == 99)
print('True' != True)
print("----------------------")


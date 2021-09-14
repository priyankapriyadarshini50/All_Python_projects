import re
text = 'This is my phone number 214-204-5959. Call me soon!'
# find 'phone' string from the text
# print(re.search('phone', text)
# create a object
pattern = 'phone'
match = re.search('phone', text)
print(match)
print(match.start())
print(match.end())
print(match.span())
print(match.string)
print(match.group())

# Find all the occurrence of the string
text1 = 'This phone is my new phone. please call me on this phone number.'
matches = re.findall(pattern, text1)
print(matches)
print(len(matches))
# TO GET THE INDEXES(start, end) OF ALL THE OCCURRENCE/string objects
for match in re.finditer(pattern,text1):
    print(match.span())
    print(match.group())

# FIND THE PHONE NUMBERS USING PATTERNS(WHEN WE DON'T KNOW THE EXACT PHONE NUMBER)
text2 = 'This is my new phone number 408-271-4545. You can also reach me at 444-202-2345. My friend ' \
        'has this number 214-629-4315'
phone_no_pattern = r'\d\d\d-\d\d\d-\d\d\d\d'
match_no = re.search(phone_no_pattern, text2)
print(match_no)
print(match_no.group())
phone_no_pattern1 = r'\d{3}-\d{3}-\d{4}'
#match1 = re.findall(phone_no_pattern1, text2)
#print(match1)
for num in re.finditer(phone_no_pattern1, text2):
    print(num.group())
print('\n')
# INSTEAD OF FOR LOOP WE CAN DIRECTLY ACCESS EACH GROUP
phone_no_pattern2 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
match2 = re.search(phone_no_pattern2, text2)
print(match2.group())
print(match2.group(1))
print(match2.group(2))
print(match2.group(3))
print("\n")

# THE OR OPERATOR
text3 = 'The man and women were present in the meeting'
pattern3 = r'man|wom\wn'
match3 = re.findall(pattern3, text3)
print(match3)
print("\n")

# WILDCARD CHARACTER
text4 = 'The cat in a hat sat here'
pattern4 = r'.at'
match4 = re.findall(pattern4, text4)
print(match4)

# FIND THE WORDS END WITH AT
text5 = 'The bat went splat'
pattern5 = r'\S+at'
match5 = re.findall(pattern5,text5)
print(match5)

# END WITH $ AND START WITH ^
match6 = re.search(r'^\d', '1 is a number')
print(match6.group())
match7 = re.search(r'\d$', 'This is number 2')
print(match7.group())

# Exclude digits
phrase = "there are 3 numbers 34 inside 5 this sentence."
exclude = r'[^\d]+'
match8 = re.findall(exclude,phrase)
print(match8)

textone = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"
fish_pattern = r'cat(fish|nap|claw)'
fish_match = re.search(fish_pattern, textone)
print(fish_match.group())

def display_led_board(num_list):
    print(num_list[1]+num_list[2]+num_list[3])
    print(num_list[4]+' '+num_list[5])
    print(num_list[6]+num_list[7]+num_list[8])
    print(num_list[9]+' '+num_list[10])
    print(num_list[11]+num_list[12]+num_list[13])


num_list = ['x', ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ']
print(len(num_list))
num = input("Ënter a number: ")
for char in num:
    if char == '1':
        num_list[1] = num_list[4] = num_list[6] = num_list[9] = num_list[11] = '#'
        display_led_board(num_list)
    if char == '2':
        num_list[1] = num_list[2] = num_list[3] = num_list[5] = num_list[8] = num_list[7] = num_list[6]\
        = num_list[9] = num_list[11] = num_list[12] = num_list[13] = '#'
        display_led_board(num_list)




def display_led(char):

    if char == '1':
        print('#')
        print('#')
        print('#')
        print('#')
        print('#')
    elif char == '2':
        print('#' * 3)
        print('  #')
        print('#' * 3)
        print('#  ')
        print('#' * 3)
    elif char == '3':
        print('#' * 3)
        print('  #')
        print('#' * 3)
        print('  #')
        print('#' * 3)
    elif char == '4':
        print('# #')
        print('# #')
        print('#' * 3)
        print('  #')
        print('  #')
    elif char == '5':
        print('#' * 3)
        print('#')
        print('#' * 3)
        print("  #")
        print('#' * 3)
    elif char == '6':
        print('#'*3)
        print('#')
        print('#'*3)
        print('# #')
        print('#'*3)
    elif char == '7':
        print('#'*3)
        print('  #')
        print('  #')
        print('  #')
        print('  #')
    elif char == '8':
        print('#'*3)
        print('# #')
        print('#'*3)
        print('# #')
        print('#'*3)
    elif char == '9':
        print('#'*3)
        print('# #')
        print('#'*3)
        print('  #')
        print('#'*3)
    elif char == '0':
        print('#'*3)
        print('# #')
        print('# #')
        print('# #')
        print('#'*3)


digits = ['1111110',  	# 0
          '0110000',  # 1
          '1101101',  # 2
          '1111001',  # 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]


def print_number(num):
	global digits
	digs = str(num)
	lines = [ '' for lin in range(5) ]
	for d in digs:
		segs = [ [' ',' ',' '] for lin in range(5) ]
		ptrn = digits[ord(d) - ord('0')]
		if ptrn[0] == '1':
			segs[0][0] = segs[0][1] = segs[0][2] = '#'
		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '#'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '#'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '#'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '#'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '#'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '#'
		for lin in range(5):
			lines[lin] += ''.join(segs[lin]) + ' '
	for lin in lines:
		print(lin)


print_number(int(input("Enter the number you wish to display: ")))



import time


def func_one(n):
    return [str(num) for num in range(n)]


def func_two(n):
    return list(map(str,range(n)))


def func_three(n):
    my_list =[]
    for i in range(n):
        my_list.append(str(i))
    return my_list


# Now calculate the elapse of each function
start_time = time.time()
# run the code
func_one(10000)
end_time = time.time()
elapse_time = end_time - start_time
print(elapse_time)

start_time2 = time.time()
# run the code
func_two(10000)
end_time2 = time.time()
elapse_time2 = end_time2 - start_time2
print(elapse_time2)

start_time3 = time.time()
# run the code
func_three(10000)
end_time3 = time.time()
elapse_time3 = end_time3 - start_time3
print(elapse_time3)


# WAY-2 TO GET THE PERFORMANCE OF THE CODE
import timeit
stmt_1 = '''
func_one(100)
'''
set_up_1 = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
print(timeit.timeit(stmt_1, set_up_1, number=10000))

stmt_2 = '''
func_two(100)
'''
set_up_2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''
print(timeit.timeit(stmt_2, set_up_2, number=10000))

stmt_3 = '''
func_three(100)
'''
set_up_3 = '''
def func_three(n):
    my_list =[]
    for i in range(n):
        my_list.append(str(i))
    return my_list
'''
print(timeit.timeit(stmt_3, set_up_3, number=10000))

def fibonacci_gen(n):
    p1 = 1
    p2 = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            res = p1 + p2
            p1, p2 = p2, res
            yield res


fib_list =[x for x in fibonacci_gen(10)]
print(fib_list)

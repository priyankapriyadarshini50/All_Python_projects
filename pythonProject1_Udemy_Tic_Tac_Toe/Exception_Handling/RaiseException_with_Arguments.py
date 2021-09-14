try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=':')
    print(e.args)

try:
    raise Exception("My exception")
except Exception as e:
    print(e, e.__str__(), sep=':')
    print(e.args)

try:
    raise Exception("exception1", "exception2")
except Exception as e:
    print(e, e.__str__(), sep=':')
    print(e.args)

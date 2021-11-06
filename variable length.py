def large(*args):
    result = args[0]
    for num in args:
        if num > result:
            result = num
    return result
print(large(10, 20, 30))
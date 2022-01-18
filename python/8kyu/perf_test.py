import timeit

# Multiply loop function with a for loop
def multiply1 (x, y):
    res = 0
    for i in range(y):
        res += x
    return res

# Multiply loop function with a while loop
def multiply2 (x, y):
    res = 0
    while y > 1:
        res += x
        y -= 1
    return res

print('multiply1', timeit.timeit('multiply1(10,10)', globals=globals()))
print('multiply2', timeit.timeit('multiply2(10,10)', globals=globals()))
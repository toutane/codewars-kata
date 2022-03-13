import math


def find_nb(m):
    sr = math.sqrt(m)
    n = 1
    while (n * (n + 1)) < (2 * sr):
        n += 1
    sum3, sum2 = 0, 0
    for i in range(n + 1):
        sum3 += math.pow(i, 3)
        sum2 += i
    print(m)
    if math.isclose(sum2**2, (n * (n + 1) / 2)**2) and math.isclose(sum2**2, m):
        return n
    else:
        return -1


print(find_nb(4396431445516211410))

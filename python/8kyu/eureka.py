# 6kyu - Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!
def is_eureka_num(n):
    res = 0
    fn, i, l = n, 0, len(str(n))
    while fn > 0:
        res += pow(fn % 10, l - i)
        i += 1
        fn = fn // 10
    return n == res

def sum_dig_pow(a, b):
    res = []
    for i in range(a, b + 1):
        if is_eureka_num(i):
            res.append(i)
    return res

print(sum_dig_pow(1, 10))